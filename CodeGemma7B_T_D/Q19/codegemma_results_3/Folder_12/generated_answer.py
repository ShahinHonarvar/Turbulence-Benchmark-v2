def all_ints_not_div_by_num(lst):
    """
            Returns the list of all integers not divisible by -26 from index 59 to index 93, both exclusive.
            If no such integers exist in the specified range, the function should return an empty list.
            """
    result = []
    for i in range(59, 93):
        if lst[i] % -26 != 0:
            result.append(lst[i])
    return result