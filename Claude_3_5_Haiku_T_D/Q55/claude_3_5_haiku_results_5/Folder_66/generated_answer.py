def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        for end in range(start, start + n):
            sublist = []
            product = 1
            idx = start
            while idx <= end:
                curr_idx = idx % n
                sublist.append(circular_list[curr_idx])
                product *= circular_list[curr_idx]
                if product == 78:
                    result.append(sublist.copy())
                    break
                if product > 78:
                    break
                idx += 1
    return result