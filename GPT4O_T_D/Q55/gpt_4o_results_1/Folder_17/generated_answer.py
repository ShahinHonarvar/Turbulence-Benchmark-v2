def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        end = start
        count = 0
        while count < n:
            product *= circular_list[end]
            if product == 18:
                if start <= end:
                    result.append(circular_list[start:end + 1])
                else:
                    result.append(circular_list[start:] + circular_list[:end + 1])
            end = (end + 1) % n
            count += 1
            if product == 0:
                break
    return result