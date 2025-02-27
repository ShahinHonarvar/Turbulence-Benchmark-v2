def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 73:
        return None
    min_num = min(numbers[31:73])
    numbers = [num for num in numbers[31:73] if num > min_num]
    if len(numbers) < 2:
        return None
    return min(numbers[1:])