def lists_with_product_equal_n(circular_list):
    if not circular_list:
        return []
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        for end in range(start, start + n):
            index = end % n
            product *= circular_list[index]
            if product == 32:
                if end - start + 1 <= n:
                    result.append([circular_list[i % n] for i in range(start, end + 1)])
            elif product == 0 or product > 32:
                break
    return result