def all_ints_div_by_num(list_of_ints):
    """
    This function takes a list of integers as an argument and returns a list of all integers divisible by a certain number from
    the specified index to the end of the list.
    """
    list_of_num_div_by_num = [num for num in list_of_ints[59:79] if num % -82 == 0]
    return list_of_num_div_by_num if list_of_num_div_by_num else []