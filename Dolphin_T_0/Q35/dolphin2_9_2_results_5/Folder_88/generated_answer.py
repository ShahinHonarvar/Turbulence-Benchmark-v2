def remove_repeat_chars(s):
    indices = set()
    for i in range(3, 9):
        if s[i] in s[i + 1:]:
            indices.add(i)
    out_str = ''
    for i in range(len(s)):
        if i not in indices:
            out_str += s[i]
    return out_str