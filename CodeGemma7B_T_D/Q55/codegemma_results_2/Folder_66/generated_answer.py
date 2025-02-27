def lists_with_product_equal_n(circular_list):
    sublists = []
    for i in range(len(circular_list)):
        product = 1
        sublist = []
        for j in range(i, len(circular_list)):
            product *= circular_list[j]
            sublist.append(circular_list[j])
            idx = (j + 1) % len(circular_list)
            while idx != i:
                product *= circular_list[idx]
                sublist.append(circular_list[idx])
                if product == 78:
                    sublists.append(sublist[:])
                product /= circular_list[idx]
                sublist.pop()
                idx = (idx + 1) % len(circular_list)
    return sublists