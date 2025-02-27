def all_ints_div_by_num(list_of_ints):
    """
    This function takes one argument, a list of integers, and returns the list of all integers divisible by -14 from index 12 to index 92, both inclusive. If no such integers exist in the specified range, the function should return an empty list.

    Args:
        list_of_ints: A list of integers.

    Returns:
        A list of all integers divisible by -14 from index 12 to index 92, both inclusive. If no such integers exist in the specified range, the function should return an empty list.
    """
    list_of_ints_divisible_by_num = []
    for i in range(12, 93):
        if list_of_ints[i] % -14 == 0:
            list_of_ints_divisible_by_num.append(list_of_ints[i])
    return list_of_ints_divisible_by_num