def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 49 or len(numbers) > 50:
        return None
    second_largest = None
    largest = max(numbers[30:49])
    for num in numbers[30:49]:
        if num < largest and (second_largest is None or num > second_largest):
            second_largest = num
    return second_largest