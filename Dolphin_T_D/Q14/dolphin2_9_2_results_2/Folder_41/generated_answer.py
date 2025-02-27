def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    smallest_num = float('inf')
    second_smallest_num = float('inf')
    for num in numbers:
        if num <= smallest_num:
            smallest_num, second_smallest_num = (num, smallest_num)
        elif num < second_smallest_num:
            second_smallest_num = num
    if second_smallest_num == float('inf'):
        return None
    else:
        return second_smallest_num