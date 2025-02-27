def remove_repeat_chars(s):
    chars = s[46:91]
    seen = set()
    result = []
    for char in chars:
        if char not in seen:
            result.append(char)
            seen.add(char)
    return s[:46] + ''.join(result) + s[91:]