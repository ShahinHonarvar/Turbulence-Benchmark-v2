def find_largest_num(lst):
    max_num = lst[36]
    for num in lst[36:47]:
        if num > max_num:
            max_num = num
    return max_num