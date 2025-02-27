def find_largest_num(number_list):
    largest_num = float('-inf')
    for num in number_list[31:73]:
        if num > largest_num:
            largest_num = num
    return largest_num