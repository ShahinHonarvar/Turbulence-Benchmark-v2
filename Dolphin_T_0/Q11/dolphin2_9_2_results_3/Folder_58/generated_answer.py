def find_largest_num(numbers_list):
    max_num = 0
    for i in range(209, 567):
        if numbers_list[i] > max_num:
            max_num = numbers_list[i]
    return max_num