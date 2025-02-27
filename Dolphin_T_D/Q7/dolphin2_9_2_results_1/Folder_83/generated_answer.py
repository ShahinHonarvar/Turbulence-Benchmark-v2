def all_even_ints_inclusive(list_of_ints):
    range_elements = list_of_ints[90:201]
    return [num for num in range_elements if num % 2 == 0]