def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 19:
        return None
    min_num1 = min(numbers[67:87])
    numbers[:] = (value for value in numbers if value > min_num1)
    if not numbers:
        return None
    min_num2 = min(numbers[67:87])
    return min_num2