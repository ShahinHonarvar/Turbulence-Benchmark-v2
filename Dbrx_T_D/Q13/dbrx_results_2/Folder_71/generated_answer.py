def find_second_largest_num(numbers):
    if len(numbers[26:53]) <= 1:
        return None
    first, second = (max(numbers[26:53]), None)
    for num in numbers[26:53]:
        if num > first:
            first, second = (num, first)
        elif num > second and num < first:
            second = num
    return second