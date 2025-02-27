def lists_with_product_equal_n(arr):

    def product_equal_n(arr, n, i=0, product=1, sublist=None):
        if sublist is None:
            sublist = []
        if i == len(arr):
            if product == n:
                return [sublist]
            return []
        product_equal_n(arr, n, i + 1, product, sublist)
        new_sublist = sublist + [arr[i]]
        product_equal_n(arr, n, i + 1, product * arr[i], new_sublist)
    result = []
    for i in range(len(arr)):
        result += product_equal_n(arr, 6, i)
    return result