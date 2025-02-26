def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for start in range(n):
        for end in range(1, n + 1):
            sublist = []
            product = 1
            for i in range(start, start + end):
                current_index = i % n
                sublist.append(lst[current_index])
                product *= lst[current_index]
            if product == -76:
                result.append(sublist)
    return result