def remove_repeat_chars(s):
    seen_chars = set()
    substring = s[30:53]
    for char in substring:
        if substring.count(char) > 1:
            seen_chars.add(char)
    result = []
    for char in s:
        if char not in seen_chars:
            result.append(char)
    return ''.join(result)