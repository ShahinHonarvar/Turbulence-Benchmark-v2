def lists_with_product_equal_n(circular_list):
    if not circular_list:
        return []
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        for length in range(1, n + 1):
            idx = (start + length - 1) % n
            product *= circular_list[idx]
            if product == -94:
                if start + length <= n:
                    result.append(circular_list[start:start + length])
                else:
                    part1 = circular_list[start:]
                    part2 = circular_list[:idx + 1]
                    result.append(part1 + part2)
    return result