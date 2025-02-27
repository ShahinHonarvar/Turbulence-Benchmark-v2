def lists_with_product_equal_n(lst, n=51):
    if not lst:
        return []
    length = len(lst)
    list_of_sublists = []
    for i in range(length):
        product = 1
        for j in range(i, i + length):
            val = lst[j % length]
            product *= val
            if product == n:
                list_of_sublists.append(lst[i:j + 1])
            elif product > n:
                break
    return list_of_sublists