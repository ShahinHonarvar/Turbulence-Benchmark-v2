def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        for j in range(1, n + 1):
            sublist = []
            product = 1
            for k in range(j):
                current_index = (i + k) % n
                current_value = lst[current_index]
                sublist.append(current_value)
                product *= current_value
            if product == 632:
                result.append(sublist)
    return result