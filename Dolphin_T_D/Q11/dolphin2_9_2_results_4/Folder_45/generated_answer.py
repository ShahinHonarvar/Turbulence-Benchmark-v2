def find_largest_num(lst):
    max_num = float('-inf')
    for num in lst[30:31]:
        if num > max_num:
            max_num = num
    return max_num