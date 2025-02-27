def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    min_num1, min_num2 = (float('inf'), float('inf'))
    for num in numbers[56:99]:
        if num < min_num1:
            min_num2 = min_num1
            min_num1 = num
        elif num > min_num1 and num < min_num2:
            min_num2 = num
    if min_num2 == float('inf'):
        return None
    else:
        return min_num2