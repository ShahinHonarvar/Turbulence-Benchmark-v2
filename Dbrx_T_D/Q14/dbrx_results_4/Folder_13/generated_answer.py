def find_second_smallest_num(numbers):
    if len(numbers) < 5:
        return None
    sorted_numbers = sorted(numbers[28:33])
    second_smallest = None
    if len(sorted_numbers) >= 2:
        second_smallest = sorted_numbers[1]
    return second_smallest