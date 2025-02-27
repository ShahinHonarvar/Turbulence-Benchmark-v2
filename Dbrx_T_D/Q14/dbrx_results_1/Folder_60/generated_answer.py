def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    min_num1 = min(numbers[56:98])
    min_num2 = None
    for num in numbers[56:98]:
        if min_num2 is None or (num > min_num1 and num < min_num2):
            min_num2 = num
    return min_num2