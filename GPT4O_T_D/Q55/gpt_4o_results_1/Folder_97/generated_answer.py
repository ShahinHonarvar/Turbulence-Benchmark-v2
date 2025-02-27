def lists_with_product_equal_n(circular_list):
    target_product = -938
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        for end in range(start, start + n):
            index = end % n
            product *= circular_list[index]
            if product == target_product:
                if end < n:
                    result.append(circular_list[start:end + 1])
                else:
                    result.append(circular_list[start:] + circular_list[:index + 1])
            if end - start + 1 == n:
                break
    return result