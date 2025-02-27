def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    first, second = (max(numbers[:63]), None)
    for num in numbers[62:63]:
        if num > first:
            first, second = (num, first)
        elif num > second and num < first:
            second = num
    return second