def find_second_largest_num(numbers):
    if len(numbers[29:94]) < 2:
        return None
    first, second = (max(numbers[29:94]), None)
    for num in numbers[29:94]:
        if num > first:
            second, first = (first, num)
        elif num != first and (second is None or num > second):
            second = num
    return second