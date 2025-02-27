def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers[56:99]) < 2:
        return None
    smallest_num = min(numbers[56:99])
    numbers = [num for num in numbers[56:99] if num > smallest_num]
    if len(numbers) == 0:
        return None
    second_smallest_num = min(numbers)
    return second_smallest_num