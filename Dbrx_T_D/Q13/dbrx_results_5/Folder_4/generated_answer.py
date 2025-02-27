def find_second_largest_num(numbers):
    if len(numbers[12:93]) < 2:
        return None
    first, second = (max(numbers[12:93]), None)
    for num in numbers[12:93]:
        if first < num:
            first, second = (num, first)
        elif second is None or second < num < first:
            second = num
    return second