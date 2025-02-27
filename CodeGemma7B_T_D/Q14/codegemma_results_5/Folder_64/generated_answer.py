def find_second_smallest_num(lst):
    if len(lst) < 5:
        return 'None'
    min_num = float('inf')
    second_min_num = float('inf')
    for num in lst[:5]:
        if num < min_num:
            min_num = num
            second_min_num = min_num
        elif num < second_min_num:
            second_min_num = num
    if second_min_num == float('inf'):
        return 'None'
    return second_min_num