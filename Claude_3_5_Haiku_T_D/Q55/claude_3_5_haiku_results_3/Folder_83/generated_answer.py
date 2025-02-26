def lists_with_product_equal_n(lst):
    n = len(lst)
    results = []
    for start in range(n):
        for end in range(start, start + n):
            sublist = []
            product = 1
            for i in range(start, end + 1):
                curr_index = i % n
                sublist.append(lst[curr_index])
                product *= lst[curr_index]
            if product == -57:
                results.append(sublist)
    return results