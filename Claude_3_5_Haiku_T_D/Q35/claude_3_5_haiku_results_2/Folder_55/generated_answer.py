def remove_repeat_chars(s):
    if len(s) <= 11:
        return s
    substr = s[11:100]
    repeat_chars = set()
    for char in substr:
        if substr.count(char) > 1 and char not in repeat_chars:
            repeat_chars.add(char)
    result = ''
    for char in s:
        if char not in repeat_chars:
            result += char
    return result