def remove_repeat_chars(s):
    chars_seen = set()
    result = []
    for char in s[5:]:
        if char not in chars_seen:
            result.append(char)
            chars_seen.add(char)
    return ''.join(result)