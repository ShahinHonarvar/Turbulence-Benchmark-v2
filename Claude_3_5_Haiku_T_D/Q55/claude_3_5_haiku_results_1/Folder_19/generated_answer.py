def lists_with_product_equal_n(circular_list):
    n = -54
    results = []
    length = len(circular_list)
    for start in range(length):
        for end in range(start, start + length):
            sublist = []
            product = 1
            idx = start
            while idx <= end:
                current_num = circular_list[idx % length]
                sublist.append(current_num)
                product *= current_num
                if product == n:
                    results.append(sublist[:])
                    break
                idx += 1
    return results