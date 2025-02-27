def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers[40:81]) < 2:
        return None
    min_num = min(numbers[40:81])
    second_num = float('inf')
    for num in numbers[40:81]:
        if num > min_num and num < second_num:
            second_num = num
    if second_num < float('inf'):
        return second_num
    else:
        return None