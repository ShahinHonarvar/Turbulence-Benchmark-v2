def find_smallest_num(list_of_numbers):
    smallest_num = list_of_numbers[0]
    if list_of_numbers[1] < smallest_num:
        smallest_num = list_of_numbers[1]
    return smallest_num