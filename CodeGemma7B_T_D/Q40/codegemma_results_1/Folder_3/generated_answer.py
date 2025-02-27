def return_n_smallest_chars(string):
    """
        Takes a string of distinct characters and returns a list of 28 characters with the smallest ASCII values.
        """
    char_ascii_list = [(char, ord(char)) for char in string]
    char_ascii_list.sort(key=lambda x: x[1], reverse=True)
    return [char for char, _ in char_ascii_list[:28]]