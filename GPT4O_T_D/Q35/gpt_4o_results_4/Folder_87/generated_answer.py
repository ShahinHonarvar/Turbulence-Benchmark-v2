def remove_repeat_chars(s):
    if len(s) <= 43:
        return s
    sample = s[21:43]
    to_remove = {char for char in sample if sample.count(char) > 1}
    return ''.join((char for char in s if char not in to_remove))