def find_largest_num(num_list):
    largest_num = num_list[10]
    for num in num_list[10:101]:
        if num > largest_num:
            largest_num = num
    return largest_num