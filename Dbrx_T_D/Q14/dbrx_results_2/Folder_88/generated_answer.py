def find_second_smallest_num(numbers):
    if len(numbers) < 9 or len(numbers[6:9]) < 2:
        return None
    min_num1 = min(numbers[6:9])
    min_num2 = None
    second_smallest_num = None
    for num in numbers[6:9]:
        if num > min_num1:
            if min_num2 is None or num < min_num2:
                min_num2 = num
                second_smallest_num = num
    return second_smallest_num