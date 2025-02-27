def all_ints_not_div_by_num(list1):
    """This function takes a list of integers as the input parameter and returns a list of all integers not divisible by -1 from index 0 to index 1, both exclusive."""
    result_list = []
    for i in range(0, 1):
        if list1[i] % -1 != 0:
            result_list.append(list1[i])
    if not result_list:
        return []
    else:
        return result_list