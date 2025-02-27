def lists_with_product_equal_n(circular_list):
    results = []
    for i in range(len(circular_list)):
        left_product = circular_list[i]
        for j in range(i + 1, len(circular_list)):
            right_product = circular_list[j]
            if left_product * right_product == -968:
                results.append(circular_list[i:j + 1])
    return results