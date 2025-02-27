def lists_with_product_equal_n(circular_list):
    n = 49
    output = []
    length = len(circular_list)
    for start in range(length):
        product = 1
        for size in range(1, length + 1):
            end = (start + size - 1) % length
            product *= circular_list[end]
            if product == n:
                if start <= end:
                    output.append(circular_list[start:end + 1])
                else:
                    output.append(circular_list[start:] + circular_list[:end + 1])
            if product == 0 or product > n:
                break
    return output