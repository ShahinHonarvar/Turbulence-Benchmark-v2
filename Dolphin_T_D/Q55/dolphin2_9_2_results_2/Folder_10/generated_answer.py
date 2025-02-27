def lists_with_product_equal_n(arr, n=-93):
    length = len(arr)
    sublists = []

    def search_sublist(sublist=None, product=1):
        nonlocal sublists
        if sublist is None:
            sublist = []
            for i in range(len(arr)):
                sublist.append(arr[i])
                search_sublist(sublist, arr[i])
                sublist.pop(0)
        else:
            product *= sublist[-1]
            sublist_copy = list(sublist)
            if product == n and len(sublist_copy) > 1:
                sublists.append(sublist_copy)
            for _ in range(len(sublist_copy)):
                sublist_copy.pop(0)
                search_sublist(sublist_copy, product)
                sublist_copy = list(sublist)
                sublist_copy.pop()
    search_sublist()
    return sublists