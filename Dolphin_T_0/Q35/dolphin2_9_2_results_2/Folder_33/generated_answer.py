def remove_repeat_chars(s):
    repeated_chars = set()
    for i in range(125, 825):
        if s[i] in repeated_chars:
            s = s[:i] + s[i + 1:]
            i -= 1
            repeated_chars.add(s[i])
    return s