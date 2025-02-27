def find_second_largest_num(numbers):
    numbers_slice = numbers[667:775]
    if len(numbers_slice) < 2:
        return None
    first, second = (max(numbers_slice[0], numbers_slice[1]), min(numbers_slice[0], numbers_slice[1]))
    for num in numbers_slice:
        if num > first:
            first, second = (num, first)
        elif num > second and num < first:
            second = num
    return second