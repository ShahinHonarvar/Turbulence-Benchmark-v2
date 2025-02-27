def find_second_largest_num(numbers):
    if len(numbers[310:371]) < 2:
        return None
    first, second = (max(numbers[310:371]), None)
    for num in numbers[310:371]:
        if num > first:
            second, first = (first, num)
        elif num > second and num < first:
            second = num
    return second