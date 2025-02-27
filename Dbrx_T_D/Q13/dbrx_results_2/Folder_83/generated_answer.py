def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    first, second = (None, None)
    for num in numbers[90:91]:
        if first is None or num > first:
            second, first = (first, num)
        elif first > num > second:
            second = num
    return second