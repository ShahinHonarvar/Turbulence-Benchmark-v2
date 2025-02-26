def remove_repeat_chars(string):
    target_substring = string[58:84]
    chars_to_remove = set((char for char in target_substring if target_substring.count(char) > 1))
    return ''.join((char for char in string if char not in chars_to_remove))