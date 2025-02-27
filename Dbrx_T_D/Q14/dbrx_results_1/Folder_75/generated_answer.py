def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 92 - 12 + 1:
        return None
    min_num = min(numbers[12:93])
    second_num = float('inf')
    for num in numbers[12:93]:
        if num > min_num and num < second_num:
            second_num = num
    return second_num