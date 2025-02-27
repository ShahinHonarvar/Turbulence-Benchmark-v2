def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:
    target_product = 990
    list_length = len(circular_list)
    sublists = []
    for i in range(list_length):
        product = 1
        sublist = []
        for j in range(i, list_length + i):
            product *= circular_list[j % list_length]
            sublist.append(circular_list[j % list_length])
            if product == target_product:
                sublists.append(sublist)
                product = 1
                sublist = []
    return sublists