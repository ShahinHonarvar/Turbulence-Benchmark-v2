def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 750 - 246 + 1:
        return None
    min_num = min(numbers[246:750])
    numbers[:] = [num for num in numbers if num > min_num]
    if not numbers:
        return None
    min_num_2 = min(numbers[246:750])
    return min_num_2