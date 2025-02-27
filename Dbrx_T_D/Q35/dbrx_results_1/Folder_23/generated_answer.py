def remove_repeat_chars(s):
    chars_taken = s[20:36]
    chars_unique = ''.join((char for index, char in enumerate(chars_taken) if chars_taken.index(char) == index))
    result = s[:20] + chars_taken.replace(chars_unique, '') + s[36:]
    return result