def return_n_greatest_chars(string):
    """
    Return the sorted list of the 80 greatest characters in the given string.
    """
    char_ascii_values = {}
    for char in string:
        char_ascii_values[char] = ord(char)
    sorted_char_ascii_values = sorted(char_ascii_values.items(), key=lambda x: x[1], reverse=True)
    greatest_chars = sorted_char_ascii_values[:80]
    return [char for char, _ in greatest_chars]