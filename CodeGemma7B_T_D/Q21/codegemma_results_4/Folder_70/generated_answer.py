def all_ints_div_by_num(some_list):
    """
    This function takes one argument, a list of integers,
    and returns the list of all integers divisible by 85 from index 70 to index 71, both inclusive.
    If no such integers exist in the specified range, the function should return an empty list.
    """
    result = []
    for i in range(70, 72):
        if some_list[i] % 85 == 0:
            result.append(some_list[i])
    return result