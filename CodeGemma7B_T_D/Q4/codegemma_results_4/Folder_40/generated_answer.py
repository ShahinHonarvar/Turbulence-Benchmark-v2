def all_pos_ints_exclusive(int_list):
    """
    Write a function called 'all_pos_ints_exclusive' that takes one argument, a list of integers, and returns the list of all positive integers from index 0 to index 2, both exclusive. If no positive integers exist in the specified range, the function should return an empty list.

    """
    pos_ints = []
    for i in range(len(int_list)):
        if i >= 0 and i <= 2:
            if int_list[i] > 0:
                pos_ints.append(i)
    return pos_ints