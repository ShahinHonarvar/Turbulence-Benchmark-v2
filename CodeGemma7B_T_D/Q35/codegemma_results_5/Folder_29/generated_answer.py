def remove_repeat_chars(string):
    result = []
    seen_chars = set()
    for char in string:
        if char in seen_chars:
            continue
        seen_chars.add(char)
        if 70 < string.index(char) < 98:
            continue
    return ''.join(result)