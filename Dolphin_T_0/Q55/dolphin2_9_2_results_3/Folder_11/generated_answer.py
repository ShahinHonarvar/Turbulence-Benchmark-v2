def lists_with_product_equal_n(lst):
    result = []
    length = len(lst)
    for i in range(length):
        for j in range(i + 1, length * 2):
            sublist = []
            for k in range(i, j):
                index = k % length
                sublist.append(lst[index])
            product = 1
            for num in sublist:
                product *= num
            if product == -15:
                result.append(sublist)
    result = [list(x) for x in set((tuple(x) for x in result))]
    return result