def remove_repeat_chars(s):
    char_count = {}
    for i, c in enumerate(s):
        if i > 40 and i < 200:
            if c in char_count:
                char_count[c] += 1
            else:
                char_count[c] = 1
    repeat_chars = [c for c, count in char_count.items() if count > 1]
    result = ''
    for c in s:
        if c not in repeat_chars:
            result += c
    return result