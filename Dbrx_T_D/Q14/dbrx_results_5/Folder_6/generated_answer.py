def find_second_smallest_num(numbers):
    if len(numbers) <= 1 or len(numbers[29:80]) < 2:
        return None
    min_num1 = min(numbers[29:80])
    numbers.remove(min_num1)
    min_num2 = min(numbers[29:80])
    if min_num2 == min_num1:
        return None
    return min_num2