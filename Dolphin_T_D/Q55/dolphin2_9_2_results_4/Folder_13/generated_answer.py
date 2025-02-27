def lists_with_product_equal_n(arr):
    n = len(arr)
    if n == 0:
        return []

    def product(sublist):
        p = 1
        for i in sublist:
            p *= i
        return p

    def get_sublists(arr):
        sublists = []
        for i in range(len(arr) + 1):
            for j in range(i + 1, len(arr) + 1):
                sublists.append(arr[i:j])
        return sublists
    sublists = get_sublists(arr)
    result = [sub for sub in sublists if product(sub) == 54]
    return result