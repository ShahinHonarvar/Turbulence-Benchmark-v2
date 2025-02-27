def all_neg_ints_exclusive(input_list):
    """Returns a list of negative integers in the specified range."""
    result = []
    for i in range(len(input_list)):
        if input_list[i] < 0 and i < 1:
            result.append(input_list[i])
    return result