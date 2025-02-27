def remove_repeat_chars(s):
    start, end = (16, 87)
    char_count = {}
    for i in range(start, end):
        if i < len(s):
            char_count[s[i]] = char_count.get(s[i], 0) + 1
    to_remove = {k for k, v in char_count.items() if v > 1}
    return ''.join((c for c in s if c not in to_remove))