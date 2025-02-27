def all_ints_div_by_both_two_nums(l: list) -> list:
    """
                    Returns a list of all integers divisible by both 22 and 82 from index 55 to index 66, both inclusive. If no such integers exist in the specified range, the function should return an empty list.
                    """
    if not isinstance(l, list):
        raise TypeError('Input must be a list')
    result = []
    for i in range(55, 67):
        if l[i] % 22 == 0 and l[i] % 82 == 0:
            result.append(l[i])
    return result