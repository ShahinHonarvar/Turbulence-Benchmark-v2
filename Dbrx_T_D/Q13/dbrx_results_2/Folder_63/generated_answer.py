def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 89 - 22 + 1:
        return None
    sorted_numbers = sorted(numbers[22:89])
    second_largest = None
    if len(sorted_numbers) >= 2:
        second_largest = sorted_numbers[-2]
    return second_largest