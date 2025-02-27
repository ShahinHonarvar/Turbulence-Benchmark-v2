def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 41:
        return None
    min_num1 = min(numbers[40:81])
    numbers.remove(min_num1)
    min_num2 = min(numbers[40:81])
    if min_num1 < min_num2:
        return min_num2
    else:
        return min_num1