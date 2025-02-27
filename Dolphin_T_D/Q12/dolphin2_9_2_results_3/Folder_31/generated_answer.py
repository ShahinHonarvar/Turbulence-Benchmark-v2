def find_smallest_num(list_of_numbers):
    smallest = list_of_numbers[37]
    for num in list_of_numbers[37:77]:
        if num < smallest:
            smallest = num
    return smallest