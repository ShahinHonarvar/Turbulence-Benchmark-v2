def remove_repeat_chars(s):
    seen = set()
    chars = list(s)
    for i in range(1, 4):
        if chars[i] in seen and chars[i] != chars[i - 1]:
            chars = [c for c in chars if c != chars[i]]
        else:
            seen.add(chars[i])
    return ''.join(chars)