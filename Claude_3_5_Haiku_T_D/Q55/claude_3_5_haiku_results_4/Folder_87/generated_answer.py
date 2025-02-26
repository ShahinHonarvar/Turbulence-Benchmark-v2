def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for start in range(n):
        for end in range(start, start + n):
            current_sublist = []
            current_product = 1
            for i in range(start, end + 1):
                index = i % n
                current_sublist.append(lst[index])
                current_product *= lst[index]
            if current_product == 27:
                result.append(current_sublist)
    return result