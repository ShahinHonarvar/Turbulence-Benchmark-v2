def find_second_smallest_num(numbers):
    if len(numbers) < 201 or len(numbers) < 50:
        return None
    min_num1 = min(numbers[49:200])
    min_num2 = None
    for num in numbers[49:200]:
        if num > min_num1:
            if min_num2 is None or num < min_num2:
                min_num2 = num
    return min_num2