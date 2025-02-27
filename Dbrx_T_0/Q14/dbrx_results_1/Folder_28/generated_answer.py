def find_second_smallest_num(numbers):
    if len(numbers) < 51 or len(numbers) > 100:
        return None
    min_num = min(numbers[21:50])
    numbers = [num for num in numbers[21:50] if num > min_num]
    if len(numbers) < 2:
        return None
    second_min_num = min(numbers[1:])
    return second_min_num