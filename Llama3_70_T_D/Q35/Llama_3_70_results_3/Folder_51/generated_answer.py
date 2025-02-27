def remove_repeat_chars(s):
    seen_chars = set(s[:6])
    for char in s[6:9]:
        seen_chars.add(char)
    result = ''
    for char in s:
        if s[6:9].count(char) > 1 and char not in seen_chars:
            continue
        elif s[6:9].count(char) > 1 and char in seen_chars:
            seen_chars.remove(char)
        else:
            result += char
    return result