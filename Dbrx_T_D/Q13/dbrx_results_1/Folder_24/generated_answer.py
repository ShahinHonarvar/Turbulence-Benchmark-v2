def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 95 or len(numbers) < 74:
        return None
    first, second = (min(numbers[74:96]), max(numbers[74:96]))
    for num in numbers[74:96]:
        if num > first:
            first, second = (num, first)
        elif num > second and num < first:
            second = num
    return second