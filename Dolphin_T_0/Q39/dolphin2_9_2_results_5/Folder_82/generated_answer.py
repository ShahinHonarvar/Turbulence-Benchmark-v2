def return_n_greatest_chars(string):
    """
    This function takes one argument, a string of distinct characters and creates 
    the sorted list of exactly 60 characters of the given string that have the
    greatest ASCII values. The function should sort the list in ascending order
    and returns it.
    """
    n = len(string)
    if n < 60:
        return None
    else:
        chars = sorted(list(filter(lambda x: string.count(x) > 0, list(string))), reverse=True)
        char_dict = {}
        for char in chars:
            char_dict[char] = string.count(char)
        sorted_chars = sorted(char_dict.items(), key=lambda x: x[0], reverse=False)
        greatest_chars = [x[0] for x in sorted_chars[:60]]
        return sorted(greatest_chars)