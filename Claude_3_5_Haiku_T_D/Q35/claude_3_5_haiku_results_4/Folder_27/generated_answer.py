def remove_repeat_chars(string):
    substring = string[87:89]
    repeat_chars = set((char for char in substring if substring.count(char) > 1))
    result = ''.join((char for char in string if char not in repeat_chars))
    return result