def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) - 1 < 54 or 50 > len(numbers) - 1:
        return None
    second_largest = None
    largest = max(numbers[50:55])
    for num in numbers[50:55]:
        if num < largest and (second_largest is None or num > second_largest):
            second_largest = num
    return second_largest