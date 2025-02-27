def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 557:
        return None
    min_num = min(numbers[208:557])
    numbers = [num for num in numbers[208:557] if num != min_num]
    if len(numbers) < 1:
        return None
    return min(numbers)