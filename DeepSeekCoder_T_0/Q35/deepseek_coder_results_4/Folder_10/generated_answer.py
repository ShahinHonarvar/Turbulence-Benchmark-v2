def remove_repeat_chars(s):
    start, end = (36, 54)
    repeat_chars = set()
    for char in s[start:end]:
        if s[start:end].count(char) > 1:
            repeat_chars.add(char)
    result = s[:start] + ''.join((c for c in s[start:end] if c not in repeat_chars)) + s[end:]
    return result