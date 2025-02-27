def find_largest_num(num_list):
    largest_num = float('-inf')
    for num in num_list[209:557]:
        if num > largest_num:
            largest_num = num
    return largest_num