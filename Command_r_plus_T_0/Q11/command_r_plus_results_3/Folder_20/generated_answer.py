def find_largest_num(numbers_list):
    largest_num = float('-inf')
    for i in range(56, 67):
        if numbers_list[i] > largest_num:
            largest_num = numbers_list[i]
    return largest_num