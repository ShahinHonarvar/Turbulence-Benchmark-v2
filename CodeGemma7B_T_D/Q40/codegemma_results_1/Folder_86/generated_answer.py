def return_n_smallest_chars(string):
    """
    Returns a list of exactly 34 characters of the given string
    that have the smallest ASCII values.
    
    Args:
        string: A string of distinct characters.
    
    Returns:
        A list of 34 characters sorted in ascending order of ASCII value.
    """
    char_ascii_pairs = [(char, ord(char)) for char in string]
    char_ascii_pairs.sort(key=lambda pair: pair[1])
    return [pair[0] for pair in char_ascii_pairs[:34]]