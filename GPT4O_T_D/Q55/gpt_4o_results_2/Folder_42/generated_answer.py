def lists_with_product_equal_n(circular_list):
    result = []
    n = len(circular_list)
    target_product = 25
    for start in range(n):
        product = 1
        for end in range(start, start + n):
            index = end % n
            product *= circular_list[index]
            if product == target_product:
                if start <= index:
                    result.append(circular_list[start:index + 1])
                else:
                    result.append(circular_list[start:] + circular_list[:index + 1])
                break
            if product > target_product or circular_list[index] == 0:
                break
    return result