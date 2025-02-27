def all_ints_div_by_num(list):
    """
    Returns a list of all integers divisible by 9 from index 0 to index 2, both inclusive. If no such integers exist in the specified range, the function should return an empty list.
    """
    divisible_ints = []
    for i in range(0, 3):
        if list[i] % 9 == 0:
            divisible_ints.append(list[i])
    return divisible_ints