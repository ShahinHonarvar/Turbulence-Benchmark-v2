def find_second_smallest_num(numbers):
    if len(numbers) < 7:
        return None
    min_num1 = min(numbers[6:7])
    min_num2 = None
    for num in numbers[6:7]:
        if num > min_num1:
            min_num2 = num
            break
    for num in numbers[7:]:
        if num < min_num1:
            min_num1, min_num2 = (num, min_num1)
        elif num < min_num2 and num > min_num1:
            min_num2 = num
    return min_num2 if min_num2 is not None else None