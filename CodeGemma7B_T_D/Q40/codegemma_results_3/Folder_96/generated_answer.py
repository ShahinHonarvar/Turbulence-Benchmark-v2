def return_n_smallest_chars(string):
    """
            Returns a list of 20 characters from the given string with the smallest ASCII values.
            """
    list_of_ascii_values = [ord(char) for char in string]
    list_of_ascii_values.sort()
    list_of_smallest_chars = []
    for i in range(20):
        list_of_smallest_chars.append(chr(list_of_ascii_values[i]))
    return list_of_smallest_chars