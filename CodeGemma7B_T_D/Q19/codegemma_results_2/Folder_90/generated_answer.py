def all_ints_not_div_by_num(int_list):
    """
    Function to return integers not divisible by -430 in a given range.

    Docstring is not part of the problem requirement.

    Parameters:
    int_list: A list of integers.

    Returns:
    A list of integers not divisible by -430 in the range [767, 905).
    If no such integers exist, an empty list is returned.
    """
    first_index = 767
    last_index = 905
    result = []
    for i in range(len(int_list)):
        if i not in range(first_index, last_index) or int_list[i] % -430 != 0:
            result.append(int_list[i])
    return result