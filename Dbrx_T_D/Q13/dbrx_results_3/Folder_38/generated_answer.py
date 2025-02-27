def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 63 - 22 + 1:
        return None
    first, second = (None, None)
    for num in numbers[22:64]:
        if first is None or num > first:
            first, second = (num, first)
        elif num < first and (second is None or num > second):
            second = num
    return second