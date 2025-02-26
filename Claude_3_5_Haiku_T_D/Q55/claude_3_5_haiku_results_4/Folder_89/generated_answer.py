def lists_with_product_equal_n(lst):
    if not lst:
        return []
    n = len(lst)
    result = []
    for start in range(n):
        for end in range(start, start + n):
            current_sublist = []
            product = 1
            for i in range(start, end + 1):
                current_index = i % n
                current_elem = lst[current_index]
                current_sublist.append(current_elem)
                product *= current_elem
                if product == 57:
                    result.append(current_sublist.copy())
    return result