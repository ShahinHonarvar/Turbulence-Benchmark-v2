def return_n_greatest_chars(str1):
    """This function takes one argument, a string of distinct characters and creates the sorted list of exactly 3 characters of the given string that have the greatest ASCII values. The function should sort the list in ascending order and returns it."""
    str2 = sorted(str1, key=ord)
    if len(str2) >= 3:
        return str2[-1::-3]
    else:
        return str2[::-1]