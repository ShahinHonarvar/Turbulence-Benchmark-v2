def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:
    target_product = -44
    list_length = len(circular_list)
    all_sublists = []
    for i in range(list_length):
        for j in range(i, i + list_length):
            sublist = circular_list[i:j]
            if len(sublist) <= list_length and sublist not in all_sublists:
                if sublist[0] == 0 or sublist[-1] == 0:
                    continue
                product = 1
                for num in sublist:
                    product *= num
                if product == target_product:
                    all_sublists.append(sublist)
    return all_sublists