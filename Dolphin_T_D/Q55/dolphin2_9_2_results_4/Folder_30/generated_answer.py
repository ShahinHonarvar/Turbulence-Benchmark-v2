def lists_with_product_equal_n(input_list):
    n = len(input_list)
    result = []
    prefix_products = [1] * n
    sufix_products = [1] * n
    total_products = [1] * n
    product = 1
    for i in range(n):
        product *= input_list[i]
        prefix_products[i] = product
    product = 1
    for i in range(n - 1, -1, -1):
        product *= input_list[i]
        sufix_products[i] = product
    for i in range(n - 1):
        total_products[i + 1] = prefix_products[i] * sufix_products[i + 1]
    for i in range(n):
        for j in range(i + 1, n + 1):
            if total_products[j] % 99 == 0 and total_products[j] // 99 == total_products[i]:
                result.append(input_list[i:j])
    return result