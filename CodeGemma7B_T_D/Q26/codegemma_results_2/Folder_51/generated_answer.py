def sum_in_range(some_list):
    """
    Sum of all integers from the given list that are between 2 and 7, both inclusive. 
    """
    result = 0
    for num in some_list:
        if num >= 2 and num <= 7:
            result += num
    return result if result else 0