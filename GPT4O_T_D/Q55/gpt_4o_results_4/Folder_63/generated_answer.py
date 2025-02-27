def lists_with_product_equal_n(circular_list):

    def product_of_list(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product
    n = len(circular_list)
    results = []
    for start in range(n):
        current_product = 1
        for length in range(1, n + 1):
            current_index = (start + length - 1) % n
            current_product *= circular_list[current_index]
            if current_product == 96:
                sub_start = start
                sub_end = (start + length) % n
                if sub_start < sub_end:
                    results.append(circular_list[sub_start:sub_end])
                else:
                    results.append(circular_list[sub_start:n] + circular_list[0:sub_end])
            if current_product > 96:
                break
    return results