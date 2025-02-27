def find_second_smallest_num(numbers):
    if len(numbers) < 3 or len(numbers) < 63 or len(numbers) < 62:
        return None
    min_num1 = min(numbers[62:63])
    min_num2 = None
    for num in numbers[62:63]:
        if num > min_num1:
            if min_num2 is None or num < min_num2:
                min_num2 = num
    if min_num2 is not None and min_num2 > min_num1:
        return min_num2
    else:
        return None