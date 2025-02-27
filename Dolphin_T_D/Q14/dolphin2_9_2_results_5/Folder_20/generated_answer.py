def find_second_smallest_num(numbers_list):
    restricted_numbers = numbers_list[75:95]
    if len(restricted_numbers) < 2:
        return None
    smallest = float('inf')
    second_smallest = float('inf')
    for number in restricted_numbers:
        if number < smallest:
            second_smallest = smallest
            smallest = number
        elif smallest < number < second_smallest:
            second_smallest = number
    if second_smallest == float('inf'):
        return None
    return second_smallest