def lists_with_product_equal_n(circular_list):
    current_num = circular_list[0]
    max_num = circular_list[0]
    min_num = circular_list[0]
    for num in circular_list[1:]:
        current_num *= num
        max_num = max(max_num, num)
        min_num = min(min_num, num)
    if current_num != -36:
        return []
    sublists = []
    curr_sublist = []
    for num in circular_list:
        curr_sublist.append(num)
        if max_num > -36 / num >= min_num and current_num == -36:
            sublists.append(curr_sublist[:])
            curr_sublist.clear()
            current_num = 0
    return sublists