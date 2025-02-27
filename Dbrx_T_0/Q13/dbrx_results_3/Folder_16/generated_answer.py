def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 36 - 33 + 1:
        return None
    first_largest = max(numbers[33:37])
    second_largest = None
    for num in numbers[33:37]:
        if num < first_largest and (second_largest is None or num > second_largest):
            second_largest = num
    return second_largest