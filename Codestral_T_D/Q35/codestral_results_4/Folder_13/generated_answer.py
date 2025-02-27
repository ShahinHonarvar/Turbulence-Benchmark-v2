def remove_repeat_chars(s):
    chars = s[46:91]
    seen = set()
    result = ''
    for char in chars:
        if char not in seen:
            result += char
            seen.add(char)
    return s[:46] + result + s[91:]