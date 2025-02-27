def find_largest_num(list_of_numbers):
    largest_num = list_of_numbers[0]
    for i in range(1, 7):
        if list_of_numbers[i] > largest_num:
            largest_num = list_of_numbers[i]
    return largest_num