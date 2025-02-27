def find_second_largest_num(lst):
    if len(lst) < 2:
        return None
    max_num = max(lst[0:10])
    second_max = float('-inf')
    for num in lst[0:10]:
        if num < max_num and num > second_max:
            second_max = num
    if second_max == float('-inf'):
        return None
    return second_max