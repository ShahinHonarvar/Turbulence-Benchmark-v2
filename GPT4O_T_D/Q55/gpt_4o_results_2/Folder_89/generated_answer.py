def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    valid_sublists = []
    circular_extended = circular_list * 2
    for start in range(n):
        product = 1
        for end in range(start, start + n):
            product *= circular_extended[end]
            if product == 57:
                valid_sublists.append(circular_extended[start:end + 1])
            if end - start >= n - 1:
                break
    return valid_sublists