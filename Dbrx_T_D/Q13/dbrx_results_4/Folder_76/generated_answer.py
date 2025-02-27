def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 301:
        return None
    sorted_numbers = sorted(numbers[686:988])
    if len(sorted_numbers) < 2:
        return None
    first_largest = sorted_numbers[-1]
    second_largest = None
    for num in sorted_numbers[:-1]:
        if num > second_largest and num < first_largest:
            second_largest = num
    return second_largest