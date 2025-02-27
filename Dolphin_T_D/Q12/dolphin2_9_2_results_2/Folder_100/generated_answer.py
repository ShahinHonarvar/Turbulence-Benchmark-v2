def find_smallest_num(lst):
    min_num = float('inf')
    for num in lst[17:78]:
        if num < min_num:
            min_num = num
    return min_num