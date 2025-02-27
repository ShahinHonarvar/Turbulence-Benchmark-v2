def all_ints_not_div_by_num(num_list):
    """Returns a list of integers not divisible by num from index 15 to index 92, exclusive."""
    if not num_list:
        return []
    result = [n for n in num_list[15:92] if n % 59 != 0]
    return result