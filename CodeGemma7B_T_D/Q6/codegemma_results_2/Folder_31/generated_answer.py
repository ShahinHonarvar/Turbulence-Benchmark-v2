from index 87 to index 95, both exclusive. If no negative integers exist in the specified range,

def all_neg_ints_exclusive(num_list):
    """
    This function takes a list of integers as an argument and returns a list of all negative integers
    the function should return an empty list.
    """
    result_list = []
    for num in num_list:
        if num < 0:
            if num_list.index(num) >= 87 and num_list.index(num) <= 94:
                result_list.append(num)
    return result_list