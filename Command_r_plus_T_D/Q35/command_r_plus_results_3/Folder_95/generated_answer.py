def remove_repeat_chars(s):
    result = []
    for char in s:
        if 32 < ord(char) < 99 and s.count(char) > 1:
            continue
        result.append(char)
    return ''.join(result)