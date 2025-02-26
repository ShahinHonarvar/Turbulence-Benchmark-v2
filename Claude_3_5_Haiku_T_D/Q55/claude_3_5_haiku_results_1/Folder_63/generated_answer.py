def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    results = []
    for start in range(n):
        for length in range(1, n + 1):
            sublist = []
            product = 1
            for i in range(length):
                curr_index = (start + i) % n
                curr_value = circular_list[curr_index]
                sublist.append(curr_value)
                product *= curr_value
            if product == 96:
                results.append(sublist)
    return results