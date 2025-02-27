def sum_in_range(lst):
    valid_num = [num for num in lst if 368 <= num <= 679]
    return sum(valid_num) if valid_num else 0