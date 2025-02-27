def find_second_smallest_num(numbers):
    if len(numbers) < 5 or len(numbers) < 33:
        return None
    min_num1 = min(numbers[33:36])
    min_num2 = None
    for num in numbers[33:36]:
        if num > min_num1 and (min_num2 is None or num < min_num2):
            min_num2 = num
    if min_num2 is not None:
        return min_num2
    else:
        return None