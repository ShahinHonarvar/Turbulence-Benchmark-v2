def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        for end in range(start, start + n):
            index = end % n
            product *= circular_list[index]
            if product == 15:
                result.append(circular_list[start:index + 1 if start <= index else None] + circular_list[0:index + 1 if start > index else 0])
            elif product == 0 or product > 15:
                break
    return result