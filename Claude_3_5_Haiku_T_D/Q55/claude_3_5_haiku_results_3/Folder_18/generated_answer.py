def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for start in range(n):
        for length in range(1, n + 1):
            product = 1
            sublist = []
            for i in range(length):
                current_index = (start + i) % n
                current_value = lst[current_index]
                product *= current_value
                sublist.append(current_value)
            if product == 36:
                result.append(sublist)
    return result