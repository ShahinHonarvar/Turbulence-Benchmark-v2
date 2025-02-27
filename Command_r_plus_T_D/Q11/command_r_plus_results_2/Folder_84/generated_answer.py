def find_largest_num(numbers_list):
    largest_num = numbers_list[43]
    for index in range(44, 87):
        if numbers_list[index] > largest_num:
            largest_num = numbers_list[index]
    return largest_num