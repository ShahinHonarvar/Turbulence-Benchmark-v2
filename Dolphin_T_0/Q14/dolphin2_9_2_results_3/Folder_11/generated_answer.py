def find_second_smallest_num(numbers_list):
    found_elements = False
    second_smallest = None
    for num in numbers_list[66:94]:
        if not found_elements:
            found_elements = True
            smallest = num
            second_smallest = num
        elif num < smallest and num != smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num
    return second_smallest