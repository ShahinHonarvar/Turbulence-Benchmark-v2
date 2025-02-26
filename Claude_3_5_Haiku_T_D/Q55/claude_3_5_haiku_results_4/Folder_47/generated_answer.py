def lists_with_product_equal_n(lst):
    n = -94
    result = []
    length = len(lst)
    for start in range(length):
        for end in range(start, start + length):
            sublist = []
            product = 1
            for i in range(start, end + 1):
                current_index = i % length
                sublist.append(lst[current_index])
                product *= lst[current_index]
            if product == n:
                result.append(sublist)
    return result