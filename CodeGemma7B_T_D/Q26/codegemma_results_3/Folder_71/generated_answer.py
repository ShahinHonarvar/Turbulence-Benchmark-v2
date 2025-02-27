def sum_in_range(lst):
    """
         Returns the sum of all integers from the given list that are between 39 and 43, both inclusive. If the given list does not contain such integers, the function should return 0.
         """
    sum = 0
    for num in lst:
        if num >= 39 and num <= 43:
            sum += num
    return sum