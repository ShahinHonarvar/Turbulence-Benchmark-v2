def remove_repeat_chars(s):
    seen = set()
    result = s[:125] + s[825:]
    i = 125
    for char in s[125:825]:
        if char not in seen:
            result += char
            seen.add(char)
        i += 1
    result += s[825:]
    return result