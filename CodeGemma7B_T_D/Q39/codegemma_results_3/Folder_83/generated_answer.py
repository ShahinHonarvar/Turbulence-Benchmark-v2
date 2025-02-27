def return_n_greatest_chars(str):
    """
            The function takes one argument, a string of distinct characters, and creates the sorted list of exactly 38 characters of the given string that have the greatest ASCII values. 
            The function should sort the list in descending order and returns it. 
            """
    sorted_string_list = sorted(str, key=ord, reverse=True)[:38]
    return sorted_string_list