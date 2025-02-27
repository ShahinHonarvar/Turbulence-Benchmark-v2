def remove_repeat_chars(s):
    seen = set()
    result = ''
    for char in s:
        if char in s[1:10] and char in seen:
            continue
        seen.add(char)
        result += char
    return result