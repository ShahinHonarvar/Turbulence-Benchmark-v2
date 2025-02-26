def remove_repeat_chars(string):
    if len(string) <= 43:
        return string
    start = 43
    end = min(87, len(string))
    substring = string[start:end]
    chars_to_remove = set((char for char in substring if substring.count(char) > 1))
    result = ''.join((char for char in string if char not in chars_to_remove))
    return result