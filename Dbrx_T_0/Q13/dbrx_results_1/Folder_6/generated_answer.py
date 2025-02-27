def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 67:
        return None
    second_largest = None
    largest = max(numbers[10:67])
    for num in numbers[10:67]:
        if num < largest and (second_largest is None or num > second_largest):
            second_largest = num
    return second_largest