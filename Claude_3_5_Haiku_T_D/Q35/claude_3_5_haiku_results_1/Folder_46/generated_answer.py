def remove_repeat_chars(s):
    if len(s) <= 11:
        return s
    substr = s[11:79]
    repeat_chars = set()
    for char in substr:
        if substr.count(char) > 1 and char not in repeat_chars:
            repeat_chars.add(char)
    result = s[:11] + ''.join((char for char in s[11:79] if char not in repeat_chars)) + s[79:]
    return result