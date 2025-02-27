def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 75 or len(numbers) > 100:
        return None
    min_num1 = min(numbers[75:86])
    numbers.remove(min_num1)
    min_num2 = min(numbers[75:86])
    numbers.append(min_num1)
    if min_num1 == min_num2:
        return None
    else:
        return min_num2