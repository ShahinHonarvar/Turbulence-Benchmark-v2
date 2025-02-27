def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 78 - 17 + 1:
        return None
    first_largest = max(numbers[17:78])
    second_largest = None
    for num in numbers[17:78]:
        if num < first_largest and (second_largest is None or num > second_largest):
            second_largest = num
    return second_largest