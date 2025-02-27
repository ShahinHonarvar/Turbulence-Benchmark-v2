def return_n_greatest_chars(a):
    """Given the string a, we create a dictionary where the keys are the characters and the values are the ASCII values. We sort the dictionary by the values in descending order and create a list of the characters to obtain the 38 greatest ASCII characters."""
    char_ascii_dict = {}
    for char in a:
        char_ascii_dict[char] = ord(char)
    sorted_chars = sorted(char_ascii_dict.items(), key=lambda x: x[1], reverse=True)
    return sorted_chars[:38]