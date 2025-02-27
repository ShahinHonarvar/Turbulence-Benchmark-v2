def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 200 or len(numbers) < 80:
        return None
    min_num1 = float('inf')
    min_num2 = float('inf')
    for num in numbers[80:201]:
        if num < min_num1:
            min_num2 = min_num1
            min_num1 = num
        elif num < min_num2 and num > min_num1:
            min_num2 = num
    if min_num2 == float('inf'):
        return None
    else:
        return min_num2