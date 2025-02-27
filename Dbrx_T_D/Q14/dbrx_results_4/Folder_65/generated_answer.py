def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers[56:58]) < 2:
        return None
    min_num = min(numbers[56:58])
    second_min_num = float('inf')
    for num in numbers[56:58]:
        if min_num < num < second_min_num:
            second_min_num = num
    return second_min_num if second_min_num < float('inf') else None