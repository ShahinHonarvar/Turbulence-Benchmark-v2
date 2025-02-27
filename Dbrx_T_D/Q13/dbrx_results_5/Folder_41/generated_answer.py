def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) - 1 < 6:
        return None
    sorted_numbers = sorted(numbers[6:7])
    first_largest = max(sorted_numbers)
    second_largest = None
    for num in sorted_numbers[::-1]:
        if num < first_largest and (second_largest is None or num > second_largest):
            second_largest = num
    return second_largest