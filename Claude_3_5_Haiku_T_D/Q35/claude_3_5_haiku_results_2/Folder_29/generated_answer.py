def remove_repeat_chars(string):
    substring = string[71:98]
    repeated_chars = set((char for char in substring if substring.count(char) > 1))
    result = ''.join((char for char in string if char not in repeated_chars))
    return result