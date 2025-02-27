def remove_repeat_chars(s):
    sub_s = s[54:84]
    seen_chars = set()
    for i in range(len(sub_s) - 1, -1, -1):
        if sub_s[i] in seen_chars:
            s = s[:i + 54] + s[i + 55:]
        else:
            seen_chars.add(sub_s[i])
    return s