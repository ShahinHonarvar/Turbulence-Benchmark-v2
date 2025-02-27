def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) - 1 < 51 or 37 > 50:
        return None
    sorted_numbers = sorted(numbers[37:52])
    if len(sorted_numbers) < 2:
        return None
    second_largest = sorted_numbers[-2]
    return second_largest