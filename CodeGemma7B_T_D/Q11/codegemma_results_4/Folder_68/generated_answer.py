def find_largest_num(num_list):
    largest_num = num_list[0]
    for num in num_list[0:9]:
        if num > largest_num:
            largest_num = num
    return largest_num