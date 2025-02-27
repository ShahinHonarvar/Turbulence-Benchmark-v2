def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 41:
        return None
    min_num1 = min(numbers[39:80])
    min_num2 = None
    for num in numbers[39:80]:
        if num > min_num1 and (min_num2 is None or num < min_num2):
            min_num2 = num
    if min_num2 is not None:
        return min_num2
    else:
        return None