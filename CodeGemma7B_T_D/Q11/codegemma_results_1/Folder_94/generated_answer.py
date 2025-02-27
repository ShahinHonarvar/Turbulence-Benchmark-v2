def find_largest_num(lst):
    max_num = lst[28]
    for num in lst[28:41]:
        if num > max_num:
            max_num = num
    return max_num