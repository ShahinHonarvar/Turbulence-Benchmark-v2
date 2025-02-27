def find_second_largest_num(numbers):
    if len(numbers[56:67]) < 2:
        return None
    first, second = (max(numbers[56:67]), None)
    for num in numbers[56:67]:
        if num > first:
            second = first
            first = num
        elif num != first and (second is None or num > second):
            second = num
    return second