def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 200 - 40 + 1:
        return None
    min_num1 = min(numbers[40:200])
    min_num2 = None
    for num in numbers[40:200]:
        if num > min_num1:
            min_num2 = num
            break
    if min_num2 is None:
        return None
    for num in numbers[40:200]:
        if num > min_num1 and num < min_num2:
            min_num2 = num
    return min_num2