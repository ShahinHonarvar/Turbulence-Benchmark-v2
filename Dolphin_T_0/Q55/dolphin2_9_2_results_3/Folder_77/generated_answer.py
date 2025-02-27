def lists_with_product_equal_n(circular_list, n=632):
    result = []
    list_length = len(circular_list)
    for i in range(list_length):
        product = 1
        for j in range(i, i + list_length):
            product *= circular_list[j % list_length]
            if product == n:
                sublist = circular_list[i:j + 1]
                if sublist not in result:
                    result.append(sublist)
    return result