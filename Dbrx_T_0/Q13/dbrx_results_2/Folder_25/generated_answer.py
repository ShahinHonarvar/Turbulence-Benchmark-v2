def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) <= 93 - 29 + 1:
        return None
    first, second = (max(numbers[29:93]), None)
    for num in numbers[29:93]:
        if num > first:
            first, second = (num, first)
        elif num != first and (second is None or num > second):
            second = num
    return second