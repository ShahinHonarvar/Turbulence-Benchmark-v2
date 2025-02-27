def return_n_greatest_chars(str_words):
    """
    Creates the sorted list of exactly 49 characters of the given string that have the greatest ASCII values.
    """
    return sorted([i for i in str_words], key=ord, reverse=True)[:49]