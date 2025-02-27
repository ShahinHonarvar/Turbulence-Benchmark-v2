def find_second_largest_num(numbers):
    subset = numbers[52:72]
    if len(subset) < 2:
        return None
    first, second = (subset[0], subset[1])
    for num in subset[2:]:
        if num > first:
            second, first = (first, num)
        elif first > num > second:
            second = num
    return second if second != subset[0] else None