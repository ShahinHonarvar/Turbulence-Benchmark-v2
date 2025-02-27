def find_largest_num(lst):
    largest_num = lst[111]
    for num in lst[111:]:
        if num > largest_num:
            largest_num = num
    return largest_num