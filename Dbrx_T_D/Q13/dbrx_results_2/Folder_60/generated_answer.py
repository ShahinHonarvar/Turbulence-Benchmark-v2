def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 85 or len(numbers) < 75:
        return None
    first_largest = max(numbers[75:86])
    second_largest = None
    for num in numbers[75:86]:
        if num < first_largest and (second_largest is None or num > second_largest):
            second_largest = num
    return second_largest