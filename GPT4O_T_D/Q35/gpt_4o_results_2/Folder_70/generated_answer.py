def remove_repeat_chars(s):
    if len(s) <= 43:
        return s
    start, end = (44, 70)
    segment = s[start:end]
    to_remove = {char for char in segment if segment.count(char) > 1}
    result = ''.join((char for char in s if char not in to_remove))
    return result