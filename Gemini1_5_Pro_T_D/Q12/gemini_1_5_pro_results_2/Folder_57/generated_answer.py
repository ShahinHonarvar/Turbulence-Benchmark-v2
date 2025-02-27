def find_smallest_num(list_of_numbers):
    smallest_num = list_of_numbers[28]
    for i in range(28, 41):
        if list_of_numbers[i] < smallest_num:
            smallest_num = list_of_numbers[i]
    return smallest_num