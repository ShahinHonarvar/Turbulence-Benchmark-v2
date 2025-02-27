def return_n_greatest_chars(chars):
    """
    :param chars: a string of distinct characters
    :return: a sorted list of the 20 greatest ASCII characters
    """
    return sorted(chars, key=ord)[-20:]