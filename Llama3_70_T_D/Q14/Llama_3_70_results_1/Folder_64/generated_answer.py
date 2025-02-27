def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    min_num = min(numbers[:5])
    numbers = [num for num in numbers[:5] if num != min_num]
    if len(numbers) == 0:
        return None
    return min(numbers)