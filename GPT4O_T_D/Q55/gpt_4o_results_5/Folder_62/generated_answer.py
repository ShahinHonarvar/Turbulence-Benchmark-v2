def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    sublists = []
    for start in range(n):
        product = 1
        for length in range(1, n + 1):
            index = (start + length - 1) % n
            product *= circular_list[index]
            if product == 100:
                end = start + length - 1
                if end < n:
                    sublists.append(circular_list[start:end + 1])
                else:
                    sublists.append(circular_list[start:] + circular_list[:end - n + 1])
            if product == 0 or product > 100:
                break
    return sublists