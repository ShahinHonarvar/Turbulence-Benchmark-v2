def all_ints_not_div_by_num(int_list):
    """
    Return the list of all integers not divisible by num from index start to index end, both exclusive. If no such integers exist, return an empty list.
    """
    if not int_list:
        return []
    try:
        int_list.index(-36)
    except ValueError:
        return []
    else:
        return [num for num in int_list[19:49] if num % -36 != 0]