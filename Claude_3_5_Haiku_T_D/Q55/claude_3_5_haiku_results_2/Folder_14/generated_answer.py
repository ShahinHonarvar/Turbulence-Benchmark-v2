def lists_with_product_equal_n(circular_list):
    n = -72
    result = []
    length = len(circular_list)
    for start in range(length):
        for end in range(start, start + length):
            sublist = []
            product = 1
            current = start
            while current <= end:
                idx = current % length
                sublist.append(circular_list[idx])
                product *= circular_list[idx]
                current += 1
                if product == n:
                    result.append(sublist.copy())
                    break
                if product > n or len(sublist) == length:
                    break
    return result