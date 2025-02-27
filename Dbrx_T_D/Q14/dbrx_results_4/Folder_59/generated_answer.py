def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    min_num1 = min(numbers[:10])
    numbers = [n for n in numbers if n > min_num1]
    if len(numbers) < 1:
        return None
    min_num2 = min(numbers[:10])
    return min_num2