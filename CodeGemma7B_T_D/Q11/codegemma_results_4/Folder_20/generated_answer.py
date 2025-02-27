def find_largest_num(num_list):
    largest_num = float('-inf')
    for num in num_list[56:67]:
        if num > largest_num:
            largest_num = num
    return largest_num