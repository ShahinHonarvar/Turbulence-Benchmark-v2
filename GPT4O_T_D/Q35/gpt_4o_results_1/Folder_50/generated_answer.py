def remove_repeat_chars(s):
    if len(s) <= 76:
        return s
    middle_section = s[14:76]
    char_count = {}
    for c in middle_section:
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1
    to_remove = {c for c, count in char_count.items() if count > 1}
    result = []
    for c in s:
        if c not in to_remove:
            result.append(c)
    return ''.join(result)