def find_smallest_num(list_of_numbers):
    smallest_num = list_of_numbers[0]
    for i in range(1, 7):
        if list_of_numbers[i] < smallest_num:
            smallest_num = list_of_numbers[i]
    return smallest_num