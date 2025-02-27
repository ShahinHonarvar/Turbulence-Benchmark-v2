def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers[37:52]) < 2:
        return None
    min_num = min(numbers[37:52])
    second_num = float('inf')
    for num in numbers[37:52]:
        if min_num < num < second_num:
            second_num = num
    return second_num