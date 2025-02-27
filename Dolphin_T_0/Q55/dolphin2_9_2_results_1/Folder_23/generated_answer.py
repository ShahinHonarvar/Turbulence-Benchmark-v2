def lists_with_product_equal_n(arr):
    if len(arr) == 0:
        return []
    n = len(arr)
    result = []
    product_set = set()
    for i in range(len(arr)):
        product = 1
        for j in range(i, len(arr)):
            product *= arr[j]
            if product in product_set:
                result.append(arr[i:j + 1])
            else:
                product_set.add(product)
    return result