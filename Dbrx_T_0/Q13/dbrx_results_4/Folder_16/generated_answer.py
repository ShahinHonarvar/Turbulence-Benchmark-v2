def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 36 - 33 + 1:
        return None
    second_largest = None
    largest = max(numbers[33:36])
    for num in numbers[33:36]:
        if num < largest and (second_largest is None or num > second_largest):
            second_largest = num
    return second_largest