def find_largest_num(number_list):
    largest_num = 0
    for i in range(66, 94):
        if number_list[i] > largest_num:
            largest_num = number_list[i]
    return largest_num