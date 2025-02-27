def find_second_largest_num(numbers):
    if len(numbers[75:95]) < 2:
        return None
    first, second = (max(numbers[75:95][0], numbers[75:95][1]), min(numbers[75:95][0], numbers[75:95][1]))
    for num in numbers[75:95][2:]:
        if num > first:
            first, second = (num, first)
        elif num > second and num < first:
            second = num
    return second