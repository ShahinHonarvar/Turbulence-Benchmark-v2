def return_n_greatest_chars(text):
    """
            Returns a list of the fourty seven greatest ASCII characters from the given string, sorted in descending order.
            """
    return sorted(text, key=ord, reverse=True)[:47]