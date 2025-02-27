def find_largest_num(num_list):
    largest_num = num_list[14]
    for num in num_list[15:65]:
        if num > largest_num:
            largest_num = num
    return largest_num