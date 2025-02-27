def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    min_num, second_min_num = (min(numbers[:10]), float('inf'))
    for num in numbers[:10]:
        if num < min_num:
            min_num, second_min_num = (num, min_num)
        elif min_num < num < second_min_num:
            second_min_num = num
    if min_num == second_min_num:
        return None
    else:
        return second_min_num