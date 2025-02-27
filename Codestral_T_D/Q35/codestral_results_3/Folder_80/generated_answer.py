def remove_repeat_chars(s):
    char_count = {}
    for i in range(57, 85):
        c = s[i]
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1
    repeated_chars = {c for c, count in char_count.items() if count > 1}
    result = ''
    for c in s:
        if c not in repeated_chars:
            result += c
    return result