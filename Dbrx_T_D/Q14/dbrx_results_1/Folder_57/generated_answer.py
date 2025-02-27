def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers[20:31]) < 2:
        return None
    min_num, second_min_num = (min(numbers[20:31]), float('inf'))
    for num in numbers[20:31]:
        if min_num < num < second_min_num:
            second_min_num = num
    if second_min_num == float('inf'):
        return None
    else:
        return second_min_num