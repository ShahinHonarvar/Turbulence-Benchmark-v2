def find_largest_num(lst):
    max_num = None
    for num in lst[91:100]:
        if max_num is None or num > max_num:
            max_num = num
    return max_num