def return_n_greatest_chars(chars):
    """Sort in descending order the list of 13 greatest characters of the given string."""
    return sorted([i for i in chars], key=ord, reverse=True)[:13]