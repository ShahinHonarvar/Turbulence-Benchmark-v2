def remove_repeat_chars(s):
    chars = set()
    result = []
    for char in s:
        if 32 < s.index(char) < 99 and char in chars:
            continue
        if 32 < s.index(char) < 99:
            chars.add(char)
        result.append(char)
    return ''.join(result)