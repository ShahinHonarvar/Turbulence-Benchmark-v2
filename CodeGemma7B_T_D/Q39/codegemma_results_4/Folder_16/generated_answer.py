def return_n_greatest_chars(char):
    """
            This function takes one argument, a string of distinct characters and creates the sorted list of exactly 64 characters of the given string that have the greatest ASCII values. Sort the list in descending order and returns it.
            """
    return sorted(char, key=ord, reverse=True)[:64]