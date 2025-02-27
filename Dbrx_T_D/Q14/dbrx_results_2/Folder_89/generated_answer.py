def find_second_smallest_num(numbers):
    if len(numbers) < 3:
        return None
    min_num1, min_num2 = (float('inf'), float('inf'))
    for num in numbers[62:64]:
        if num < min_num1:
            min_num2 = min_num1
            min_num1 = num
        elif num < min_num2 and num > min_num1:
            min_num2 = num
    return min_num2 if min_num2 != float('inf') else None