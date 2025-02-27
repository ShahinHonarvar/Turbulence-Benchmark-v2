def find_smallest_num(list_of_numbers):
    smallest = None
    for num in list_of_numbers[55:99]:
        if smallest is None or num < smallest:
            smallest = num
    return smallest