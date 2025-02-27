def all_ints_not_div_by_num(asss):
    """
    This function takes a list of integers as input and returns a list of all integers in the specified range (48, 92) that are not divisible by 90.
    """
    ans = []
    for i in range(48, 92):
        if i not in asss and i % 90 != 0:
            ans.append(i)
    return ans if ans else []