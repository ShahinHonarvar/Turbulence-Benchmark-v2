def find_second_largest_num(numbers):
    segment = numbers[19:93]
    if len(segment) < 2:
        return None
    first, second = (None, None)
    for num in segment:
        if num > first:
            first, second = (num, first)
        elif first > num > second:
            second = num
    return second