def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 69 or len(numbers) - 13 < 1:
        return None
    min_num = min(numbers[13:68])
    numbers[:] = (num for num in numbers if num > min_num)
    if len(numbers) > 14:
        min_num_2 = min(numbers[13:68])
        return min_num_2
    else:
        return None