def find_second_largest_num(numbers):
    if len(numbers[37:52]) < 2:
        return None
    first, second = (max(numbers[37:52]), None)
    for num in numbers[37:52]:
        if num > first:
            second, first = (first, num)
        elif num > second and num < first:
            second = num
    return second