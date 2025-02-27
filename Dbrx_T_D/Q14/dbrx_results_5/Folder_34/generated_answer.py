def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers[60:200]) < 2:
        return None
    min_num1 = min(numbers[60:200])
    min_num2 = None
    for num in numbers[60:200]:
        if num > min_num1:
            min_num2 = num
            break
    for num in numbers[60:200]:
        if min_num1 < num < min_num2:
            min_num2 = num
    return min_num2