def lists_with_product_equal_n(circular_list):
    for i in range(len(circular_list)):
        product = circular_list[i]
        sublist = [circular_list[i]]
        j = i + 1
        while j % len(circular_list) != i:
            if product * circular_list[j] != -81:
                product = product * circular_list[j]
                sublist.append(circular_list[j])
            j += 1
        if product == -81:
            yield sublist