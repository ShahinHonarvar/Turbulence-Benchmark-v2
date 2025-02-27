def find_second_smallest_num(numbers):
    if len(numbers) < 50 or len(numbers) > 50:
        return None
    min_num = min(numbers[34:50])
    numbers.remove(min_num)
    if len(numbers) < 50 or len(numbers) > 50:
        return None
    min_num2 = min(numbers[34:50])
    if min_num2 == min_num:
        return None
    else:
        return min_num2