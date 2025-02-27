def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 42 or len(numbers) < 68:
        return None
    min_num1 = min(numbers[42:69])
    numbers.remove(min_num1)
    min_num2 = min(numbers[42:69])
    if min_num1 == min_num2:
        return None
    else:
        return min_num2