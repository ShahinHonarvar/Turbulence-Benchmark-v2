def find_second_largest_num(lst):
    if len(lst) < 2:
        return None
    max_num = second_max = float('-inf')
    for num in lst:
        if num > max_num:
            max_num, second_max = (num, max_num)
        elif num != max_num and num > second_max:
            second_max = num
    return second_max if second_max != float('-inf') else None