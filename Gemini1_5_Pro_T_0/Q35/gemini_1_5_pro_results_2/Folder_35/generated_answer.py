def remove_repeat_chars(s):
    seen = set()
    result = ''
    for i, char in enumerate(s):
        if 77 < i < 84:
            if char in s[78:84] and char not in seen:
                seen.add(char)
            else:
                continue
        result += char
    return result