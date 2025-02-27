def remove_repeat_chars(s):
    seen = set()
    result = ''
    for i, char in enumerate(s):
        if 18 < i < 60 and char in s[i + 1:60] and (char not in seen):
            seen.add(char)
        else:
            result += char
    return result