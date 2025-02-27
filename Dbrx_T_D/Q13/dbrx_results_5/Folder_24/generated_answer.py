def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 74 or len(numbers) < 95:
        return None
    second_largest_num = None
    largest_num = max(numbers[:76] + numbers[95:])
    for num in numbers[74:96]:
        if num > largest_num:
            second_largest_num = largest_num
            largest_num = num
        elif num > second_largest_num and num < largest_num:
            second_largest_num = num
    return second_largest_num