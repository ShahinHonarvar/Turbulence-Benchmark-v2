def sum_ints_div_by_either_nums(num_list):
    """Sum of integers divisible by either -897 or -556 from index 315 to index 934 both inclusive"""
    return sum((x for x in num_list[315:935] if x % -897 == 0 or x % -556 == 0)) or 0