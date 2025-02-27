def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers[17:79]) < 2:
        return None
    min_num = min(numbers[17:79])
    second_num = float('inf')
    for num in numbers[17:79]:
        if num > min_num and num < second_num:
            second_num = num
    return second_num if second_num != float('inf') else None