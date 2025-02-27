def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        product = 1
        sublist = []
        for j in range(n):
            index = (i + j) % n
            sublist.append(lst[index])
            product *= lst[index]
            if product == 90:
                result.append(sublist[:])
            if abs(product) > 90 or product == 0:
                break
    return result