def lists_with_product_equal_n(circular_list):
    for i in range(len(circular_list)):
        prefix_product = circular_list[i]
        for j in range(i + 1, len(circular_list)):
            suffix_product = circular_list[j]
            k = j + 1
            while k < len(circular_list) or k < i:
                if prefix_product * suffix_product == -32:
                    return [[circular_list[i]]]
                elif prefix_product * suffix_product > -32:
                    break
                prefix_product *= circular_list[k]
                suffix_product *= circular_list[(k - 1) % len(circular_list)]
                k += 1
    return []