def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for start in range(n):
        for end in range(start, start + n):
            sublist = []
            product = 1
            current_index = start
            while current_index <= end:
                current_value = lst[current_index % n]
                product *= current_value
                sublist.append(current_value)
                if product == 0:
                    result.append(sublist.copy())
                    break
                current_index += 1
    return result