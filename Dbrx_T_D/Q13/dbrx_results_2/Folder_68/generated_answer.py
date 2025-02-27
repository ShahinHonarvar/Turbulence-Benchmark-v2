def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) > 9:
        return None
    first, second = max(numbers[0:2])
    for num in numbers[2:]:
        if num > first:
            first, second = (num, first)
        elif num > second and num < first:
            second = num
    if second == 0:
        return None
    else:
        return second