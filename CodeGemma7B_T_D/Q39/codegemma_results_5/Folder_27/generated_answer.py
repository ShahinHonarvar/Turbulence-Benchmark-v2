def return_n_greatest_chars(text):
    """
        Write a function called 'return_n_greatest_chars' that takes one argument, a string of distinct characters and creates the sorted list of exactly 82 characters of the given string that have the greatest ASCII values. The function should sort the list in ascending order and returns it.
        """
    return sorted(text, key=ord)[-82:]