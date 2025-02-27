def lists_with_product_equal_n(n, arr):

    def get_product(arr):
        product = 1
        for i in arr:
            product *= i
        return product

    def get_sublists(arr):
        sublists = []
        for i in range(len(arr)):
            for j in range(i + 1, len(arr) + 1):
                sublists.append(arr[i:j])
        return sublists
    sublists = get_sublists(arr)
    result = []
    for sublist in sublists:
        if get_product(sublist) == n:
            result.append(sublist)
    return result