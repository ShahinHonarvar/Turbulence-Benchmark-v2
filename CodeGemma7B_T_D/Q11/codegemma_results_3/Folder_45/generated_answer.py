def find_largest_num(number_list):
    max_num = float('-inf')
    for num in number_list[30:31]:
        if num > max_num:
            max_num = num
    return max_num