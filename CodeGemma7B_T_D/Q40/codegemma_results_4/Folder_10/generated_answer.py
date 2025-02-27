def return_n_smallest_chars(string):
    """
            Returns a list of exactly 88 characters of the given string that have the smallest ASCII values.
            The list is sorted in descending order.
            """
    list_of_chars = sorted(string, key=ord)
    return_list = list_of_chars[:88]
    return return_list