def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 98 or len(numbers) - 42 < 56:
        return None
    first, second = (max(numbers[56:98]), None)
    for num in numbers[:56] + numbers[98:]:
        if num > first:
            first, second = (num, first)
        elif num > second:
            second = num
    if second is None:
        return None
    else:
        return second