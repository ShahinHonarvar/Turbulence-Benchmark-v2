def lists_with_product_equal_n(circular_list):
    n = -36
    found_sublists = []
    for i in range(len(circular_list)):
        product = circular_list[i]
        for j in range(i + 1, len(circular_list)):
            product *= circular_list[j]
            if product == n:
                sublist = circular_list[i:j + 1]
                found_sublists.append(sublist)
                while i > 0 and sublist == circular_list[i - 1:j + 1]:
                    i -= 1
    return found_sublists