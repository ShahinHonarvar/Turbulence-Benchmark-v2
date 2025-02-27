def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 556 - 209 + 1:
        return None
    first, second = (max(numbers[209:557]), None)
    for num in numbers[209:557]:
        if num > first:
            first, second = (num, first)
        elif num != first and (second is None or num > second):
            second = num
    return second