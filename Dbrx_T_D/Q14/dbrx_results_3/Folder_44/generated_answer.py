def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers[90:100]) < 2:
        return None
    min_num = min(numbers[90:100])
    second_min_num = float('inf')
    for num in numbers[90:100]:
        if num > min_num and num < second_min_num:
            second_min_num = num
    return second_min_num if second_min_num < float('inf') else None