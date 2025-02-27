def find_second_smallest_num(numbers):
    if len(numbers) < 30:
        return None
    min_num1 = numbers[30]
    min_num2 = None
    for i in range(31, 201):
        if i >= len(numbers):
            break
        num = numbers[i]
        if num <= min_num1:
            min_num2 = min_num1
            min_num1 = num
        elif num < min_num2 or min_num2 > min_num1:
            min_num2 = num
    if min_num2 is None or min_num2 >= min_num1:
        return None
    else:
        return min_num2