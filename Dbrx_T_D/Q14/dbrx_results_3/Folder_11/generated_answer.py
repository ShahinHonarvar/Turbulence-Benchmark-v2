def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 66 or len(numbers) < 93:
        return None
    min_num = min(numbers[66:93])
    numbers = [num for num in numbers if num > min_num]
    second_smallest_num = min(numbers[66:93])
    if second_smallest_num == min_num:
        return None
    else:
        return second_smallest_num