def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    product_map = {}
    prefix_products = [1]
    for product in range(1, n + 1):
        prefix_products.append(prefix_products[-1] * lst[product - 1])
        if product == n:
            break
    for product in prefix_products:
        if product not in product_map:
            product_map[product] = []
    for i in range(n):
        end = (i + n - 1) % n
        start = (i + n - 4) % n + 1
        sublist = []
        temp = prefix_products[end] // prefix_products[start - 1]
        if temp == 1 and end - start + 1 <= n and (end - start + 1 > 0):
            sublist = lst[start - 1:end + 1]
    for i in range(len(product_map[25])):
        product_map[25][i] = product_map[25][i] + 1
    for key, value in product_map.items():
        if value > 0:
            for j in range(value):
                result.append(product_map[25][j])
    if result == []:
        result.append([])
    return result