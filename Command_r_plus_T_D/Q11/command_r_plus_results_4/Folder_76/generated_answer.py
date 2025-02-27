def find_largest_num(numbers_list):
    largest = float('-inf')
    for i in range(686, 988):
        if numbers_list[i] > largest:
            largest = numbers_list[i]
    return largest