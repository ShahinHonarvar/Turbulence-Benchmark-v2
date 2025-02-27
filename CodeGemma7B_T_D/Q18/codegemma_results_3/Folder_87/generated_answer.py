def sum_ints_div_by_either_nums(lst):
    """
    Returns the sum of all integers divisible by either 15 or 57 from index 18 to index 52, both inclusive. If no such integers exist in the specified range, the function should return 0.
    """
    sum_nums = 0
    for i in range(18, 53):
        if lst[i] % 15 == 0 or lst[i] % 57 == 0:
            sum_nums += lst[i]
    if sum_nums == 0:
        return 0
    else:
        return sum_nums