def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 95:
        return None
    max_num = max(numbers[74:95])
    max2_num = None
    for num in numbers[74:95]:
        if num != max_num and (max2_num is None or num > max2_num):
            max2_num = num
    return max2_num