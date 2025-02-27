def find_largest_num(lst):
    max_num = lst[0]
    for num in lst[0:8]:
        if num > max_num:
            max_num = num
    return max_num