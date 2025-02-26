def remove_repeat_chars(string):
    if len(string) <= 14:
        return string
    substring = string[14:70]
    repeated_chars = set((char for char in substring if substring.count(char) > 1))
    result = ''.join((char for char in string if char not in repeated_chars or substring.count(char) <= 1))
    return result