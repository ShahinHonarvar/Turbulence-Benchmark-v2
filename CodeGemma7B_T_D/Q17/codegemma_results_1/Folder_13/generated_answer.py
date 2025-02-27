def all_ints_div_by_both_two_nums(num_list):
    """
    Returns all integers divisible by both 45 and 20 from index 13 to index 18, both inclusive.
    """
    return [num for num in num_list[13:19] if num % 45 == 0 and num % 20 == 0]