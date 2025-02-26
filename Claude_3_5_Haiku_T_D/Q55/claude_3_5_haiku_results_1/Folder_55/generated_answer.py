def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        for end in range(start, start + n):
            sublist = []
            product = 1
            current = start
            while current <= end:
                sublist.append(circular_list[current % n])
                product *= circular_list[current % n]
                current += 1
                if product == -6:
                    result.append(sublist.copy())
                if product < -6:
                    break
    return result