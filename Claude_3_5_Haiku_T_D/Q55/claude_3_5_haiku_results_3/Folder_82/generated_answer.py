def lists_with_product_equal_n(lst):
    if not lst:
        return []
    n = 8
    result = []
    length = len(lst)
    for start in range(length):
        for end in range(start, start + length):
            sublist = []
            product = 1
            for i in range(start, end + 1):
                index = i % length
                sublist.append(lst[index])
                product *= lst[index]
            if product == n and len(sublist) > 0:
                result.append(sublist)
    return result