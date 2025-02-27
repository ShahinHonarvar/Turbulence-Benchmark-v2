def return_n_smallest_chars(str):
    """
          This function takes one argument, a string of distinct characters, and 
          creates a list of exactly 60 characters that have the smallest ASCII values.
          The function sorts the list in ascending order and returns the list.
          """
    str_list = list(str)
    str_list.sort(key=ord)
    if len(str_list) <= 60:
        return str_list[:len(str_list)]
    else:
        return str_list[:60]