def find_largest_num(num_list):
    largest_num = num_list[1]
    for num in num_list[1:6]:
        if num > largest_num:
            largest_num = num
    return largest_num