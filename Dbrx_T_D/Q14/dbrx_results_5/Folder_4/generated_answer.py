def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 85:
        return None
    min_num1 = min(numbers[70:85])
    min_num2 = None
    for num in numbers[70:85]:
        if num > min_num1 and (min_num2 is None or num < min_num2):
            min_num2 = num
    return min_num2