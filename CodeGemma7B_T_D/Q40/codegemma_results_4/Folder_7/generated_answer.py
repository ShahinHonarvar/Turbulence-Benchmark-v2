def return_n_smallest_chars(string):
    list_of_ascii_codes = sorted([ord(char) for char in string])
    return list_of_ascii_codes[:49]