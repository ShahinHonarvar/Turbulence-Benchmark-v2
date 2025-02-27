def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 99:
        return None
    second_largest = None
    largest = max(numbers[55:98])
    for num in numbers[55:98]:
        if num < largest and (second_largest is None or num > second_largest):
            second_largest = num
    return second_largest