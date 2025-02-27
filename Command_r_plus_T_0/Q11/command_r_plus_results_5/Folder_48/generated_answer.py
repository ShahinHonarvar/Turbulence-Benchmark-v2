def find_largest_num(numbers_list):
    largest = float('-inf')
    for i in range(533, 606):
        if numbers_list[i] > largest:
            largest = numbers_list[i]
    return largest