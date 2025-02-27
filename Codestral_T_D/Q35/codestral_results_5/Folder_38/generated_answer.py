def remove_repeat_chars(s):
    result = ''
    seen = set()
    for char in s[36:85]:
        if char not in seen and s.count(char) > 1:
            seen.add(char)
        if char not in seen:
            result += char
    return result