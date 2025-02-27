def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 95 or len(numbers) < 74:
        return None
    min_num1 = min(numbers[74:96])
    numbers.remove(min_num1)
    min_num2 = min(numbers[74:96])
    if min_num2 == min_num1:
        return None
    return min_num2