def insert_after_index(lst):
    """
    Given a list, this function returns a new list identical to the original except that [15, 51] has been 
    inserted at the index immediately succeeding index 76.
    """
    return lst[:77] + [15, 51] + lst[77:]