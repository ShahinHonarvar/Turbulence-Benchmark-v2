def return_n_smallest_chars(text):
    """
   This function takes in a string of distinct characters and returns a list of the smallest ASCII values in descending order.
   """
    char_list = list(text)
    char_list.sort(key=ord)
    return char_list[:84][::-1]