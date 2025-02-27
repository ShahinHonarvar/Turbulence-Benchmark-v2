def lists_with_product_equal_n(n, arr):

    def get_sublists(i, sublist, product, result):
        if i == len:
            if product == target:
                result.append(sublist + [val])
            return
        get_sublists(i + 1, sublist + [val], product * val, result)
        get_sublists(i + 1, sublist, product / val, result)
    target, len = (n, len(arr))
    result = []
    for val in arr:
        for i in range(len):
            get_sublists(0, [], 1, result)
    return result