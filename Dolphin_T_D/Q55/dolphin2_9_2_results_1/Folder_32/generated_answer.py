def lists_with_product_equal_n(circular_list):
    size = len(circular_list)
    product_76 = []
    for size_sublist in range(1, size + 1):
        for start in range(size):
            product = 1
            for index in range(start, start + size_sublist):
                if index >= size:
                    index = index - size
                product *= circular_list[index]
            if product == 76:
                sublist = []
                for index in range(start, start + size_sublist):
                    if index >= size:
                        index = index - size
                    sublist.append(circular_list[index])
                product_76.append(sublist)
    return product_76