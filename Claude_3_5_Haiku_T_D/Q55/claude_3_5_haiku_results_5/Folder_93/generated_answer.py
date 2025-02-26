def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for start in range(n):
        for end in range(start, start + n):
            sublist = []
            product = 1
            current_index = start
            while current_index <= end:
                idx = current_index % n
                sublist.append(lst[idx])
                product *= lst[idx]
                current_index += 1
                if product == -91:
                    result.append(sublist.copy())
                if product < -91:
                    break
    return result