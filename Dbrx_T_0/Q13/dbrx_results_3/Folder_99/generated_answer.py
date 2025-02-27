def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    first, second = (max(numbers[:60]), None)
    for num in numbers[60:110]:
        if num > first:
            first, second = (num, first)
        elif num > second and num < first:
            second = num
    return second