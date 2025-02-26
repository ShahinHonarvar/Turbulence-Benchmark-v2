def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        for end in range(start, start + n):
            sublist = []
            product = 1
            idx = start
            while idx <= end:
                current_elem = circular_list[idx % n]
                sublist.append(current_elem)
                product *= current_elem
                if product == -779:
                    result.append(sublist.copy())
                idx += 1
    return result