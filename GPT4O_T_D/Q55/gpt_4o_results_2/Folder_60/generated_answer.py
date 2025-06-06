def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        for end in range(start, start + n):
            index = end % n
            product *= circular_list[index]
            if product == 49:
                result.append([circular_list[i % n] for i in range(start, end + 1)])
            elif product > 49 or product == 0:
                break
    return result