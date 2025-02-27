def remove_repeat_chars(s):
    char_count = {}
    for c in s[16:87]:
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1
    result = ''
    for c in s:
        if c not in char_count or char_count[c] < 2:
            result += c
    return result