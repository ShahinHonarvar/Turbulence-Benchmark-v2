def return_n_smallest_chars(input_string):
    """
        Returns a list of 20 character strings of the given input string 
        with the smallest ASCII values sorted in ascending order.
        """
    chars = list(input_string)
    chars.sort()
    return chars[:20]