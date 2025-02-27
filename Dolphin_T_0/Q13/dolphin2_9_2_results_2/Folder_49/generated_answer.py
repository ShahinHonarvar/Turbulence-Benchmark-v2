def find_second_largest_num(lst):
    sliced_lst = lst[80:201]
    if len(sliced_lst) < 2:
        return None
    first = second = -float('inf')
    for num in sliced_lst:
        if num > first:
            first = num
        elif first > num > second:
            second = num
    if second == -float('inf'):
        return None
    return second