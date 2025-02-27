def find_second_largest_num(lst):
    if len(lst) < 5:
        return None
    max_num = max(lst[4])
    second_max_num = None
    for num in lst[4]:
        if num != max_num and (second_max_num == None or num > second_max_num):
            second_max_num = num
    return second_max_num