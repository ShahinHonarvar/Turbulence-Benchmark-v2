def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        for end in range(start, start + n):
            sublist = []
            product = 1
            idx = start
            while idx <= end:
                curr = circular_list[idx % n]
                sublist.append(curr)
                product *= curr
                if product == 990:
                    result.append(sublist.copy())
                    break
                if product > 990:
                    break
                idx += 1
    return result