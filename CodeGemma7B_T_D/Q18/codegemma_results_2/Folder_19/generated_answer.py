def sum_ints_div_by_either_nums(lst):
    """sum of all integers divisible by either 4 or -6 from index 1 to index 4, both inclusive"""
    return sum((num for num in lst[1:5] if num % 4 == 0 or num % -6 == 0)) or 0