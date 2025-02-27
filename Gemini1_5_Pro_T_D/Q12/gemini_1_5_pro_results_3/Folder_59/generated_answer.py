def find_smallest_num(list_of_numbers):
    smallest = list_of_numbers[0]
    for i in range(1, 9):
        if list_of_numbers[i] < smallest:
            smallest = list_of_numbers[i]
    return smallest