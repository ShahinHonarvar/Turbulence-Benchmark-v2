def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) <= 17 or len(numbers) > 78:
        return None
    min_num1 = min(numbers[17:78])
    numbers.remove(min_num1)
    min_num2 = None
    for num in numbers[17:78]:
        if num > min_num1:
            if min_num2 is None or num < min_num2:
                min_num2 = num
    return min_num2