def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 68 - 42 + 1:
        return None
    second_largest = None
    largest = max(numbers[42:69])
    for num in numbers[42:69]:
        if num < largest and (second_largest is None or num > second_largest):
            second_largest = num
    if second_largest is None:
        return None
    return second_largest