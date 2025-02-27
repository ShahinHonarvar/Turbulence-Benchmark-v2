def lists_with_product_equal_n(lst):
    n = len(lst)
    lists = []
    for i in range(n):
        product = 1
        traversed = []
        node = lst[i]
        while traversed.count(node) == 0:
            product *= node
            traversed.append(node)
            node = lst[(lst.index(node) + 1) % n]
            if product == -15:
                lists.append(list(traversed))
        if len(lists) > 0:
            return lists
    return []