def remove_repeat_chars(s):
    chars = {}
    result = []
    for char in s[1:10]:
        if char in chars:
            continue
        chars[char] = None
        result.append(char)
    return ''.join(result) + s[10:]