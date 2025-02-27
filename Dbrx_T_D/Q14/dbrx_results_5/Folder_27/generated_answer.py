def find_second_smallest_num(numbers):
    if len(numbers) < 60:
        return None
    min_num1 = min(numbers[25:60])
    numbers.remove(min_num1)
    min_num2 = min(numbers[24:59])
    if min_num1 == min_num2:
        return None
    else:
        return min_num2