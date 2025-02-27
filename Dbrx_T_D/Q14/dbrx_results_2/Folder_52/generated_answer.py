def find_second_smallest_num(numbers):
    if len(numbers) < 3 or len(numbers[64:67]) < 2:
        return None
    first_two_smallest = [numbers[64], numbers[64]]
    for num in numbers[65:68]:
        if num < first_two_smallest[0]:
            first_two_smallest = [num, first_two_smallest[0]]
        elif num < first_two_smallest[1]:
            first_two_smallest[1] = num
    return first_two_smallest[1] if first_two_smallest[0] != first_two_smallest[1] else None