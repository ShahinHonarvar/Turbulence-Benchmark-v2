def remove_repeat_chars(s):
    substring = s[91:97]
    repeat_chars = set()
    for char in substring:
        if substring.count(char) > 1:
            repeat_chars.add(char)
    result = ''.join((char for char in s if char not in repeat_chars))
    return result