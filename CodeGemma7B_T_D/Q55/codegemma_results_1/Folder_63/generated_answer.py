def lists_with_product_equal_n(circular_list):
    for i in range(len(circular_list)):
        prod = circular_list[i]
        for j in range(i + 1, len(circular_list)):
            prod *= circular_list[j]
            if prod == 96:
                yield [circular_list[k] for k in range(i, j + 1)]
            elif prod > 96:
                break