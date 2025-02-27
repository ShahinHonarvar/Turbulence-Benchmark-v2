def lists_with_product_equal_n(circular_list):
    n = 93
    results = []
    length = len(circular_list)
    for start in range(length):
        product = 1
        for end in range(start, start + length):
            index = end % length
            product *= circular_list[index]
            if product == n:
                if end >= start:
                    results.append(circular_list[start:end + 1])
                else:
                    results.append(circular_list[start:] + circular_list[:index + 1])
            if product == 0:
                break
            if product > n:
                break
            if product != n and start == end:
                product = circular_list[index]
    return results