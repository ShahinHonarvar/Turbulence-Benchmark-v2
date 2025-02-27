def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 19 or len(numbers) > 92:
        return None
    first, second = (max(numbers[19:93]), None)
    for num in numbers[19:93]:
        if num > first:
            second, first = (first, num)
        elif num > second and num < first:
            second = num
    return second