def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    min_num = max_num = numbers[66]
    second_max_num = None
    for num in numbers[67:94]:
        if num > max_num:
            second_max_num = max_num
            max_num = num
        elif num > min_num and num < max_num:
            second_max_num = num
    return second_max_num