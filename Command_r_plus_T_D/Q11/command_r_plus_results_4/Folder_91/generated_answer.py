def find_largest_num(numbers_list):
    largest = numbers_list[0]
    for index in range(1, 6):
        if numbers_list[index] > largest:
            largest = numbers_list[index]
    return largest