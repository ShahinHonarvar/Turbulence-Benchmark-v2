def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 50:
        return None
    min_num = min(numbers[29:80])
    numbers = [num for num in numbers[29:80] if num > min_num]
    if len(numbers) < 1:
        return None
    second_min_num = min(numbers)
    return second_min_num