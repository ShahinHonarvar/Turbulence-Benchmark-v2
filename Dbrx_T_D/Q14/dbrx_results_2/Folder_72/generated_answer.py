def find_second_smallest_num(numbers):
    if not numbers or len(numbers) < 2:
        return None
    smallest_num = min(numbers[82:87])
    second_smallest_num = float('inf')
    for num in numbers[82:87]:
        if smallest_num < num < second_smallest_num:
            second_smallest_num = num
    if second_smallest_num != float('inf'):
        return second_smallest_num
    else:
        return None