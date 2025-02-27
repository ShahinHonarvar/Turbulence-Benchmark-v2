def all_ints_div_by_num(num_list):
    """Returns a list of all integers divisible by 86 from index 86 to index 92, both inclusive."""
    filtered_list = [num for num in num_list[86:93] if num % 86 == 0]
    return filtered_list if filtered_list else []