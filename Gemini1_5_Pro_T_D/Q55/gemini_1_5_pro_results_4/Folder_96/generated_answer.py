def lists_with_product_equal_n(circular_list):
    sublists = []
    for start in range(len(circular_list)):
        for end in range(start + 1, len(circular_list) + 1):
            sublist = circular_list[start:end]
            if 0 in sublist:
                sublists.append(sublist)
            else:
                product = 1
                for x in sublist:
                    product *= x
                if product == 0:
                    sublists.append(sublist)
    return sublists