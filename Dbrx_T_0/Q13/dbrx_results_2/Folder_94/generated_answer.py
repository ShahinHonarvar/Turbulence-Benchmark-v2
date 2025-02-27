def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 40 or len(numbers) < 28:
        return None
    first_largest = max(numbers[28:41])
    second_largest = None
    for num in numbers[28:41]:
        if num < first_largest and (second_largest is None or num > second_largest):
            second_largest = num
    return second_largest