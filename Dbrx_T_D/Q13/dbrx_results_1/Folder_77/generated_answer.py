def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) >= 539:
        return None
    first, second = (None, None)
    for num in numbers[527:539]:
        if first is None or first <= num:
            second = first
            first = num
        elif second is None or second < num:
            second = num
    if second is None:
        return None
    else:
        return second