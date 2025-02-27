def return_n_greatest_chars(string):
    ascii_chars = [ord(char) for char in string if string.count(char) == 1]
    ascii_chars.sort(reverse=True)
    return [chr(char) for char in ascii_chars[:82]]