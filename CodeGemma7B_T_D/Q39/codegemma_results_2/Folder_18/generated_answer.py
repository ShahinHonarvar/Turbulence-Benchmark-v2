def return_n_greatest_chars(text):
    """
          Return the list of n greatest characters from the given text.
          """
    return sorted(text, key=ord, reverse=True)[:52]