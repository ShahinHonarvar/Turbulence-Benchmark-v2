def remove_repeat_chars(s):
    char_count = {}
    for i in range(52, 76):
        if s[i] in char_count:
            char_count[s[i]] += 1
        else:
            char_count[s[i]] = 1
    repeat_chars = {k for k, v in char_count.items() if v > 1}
    return ''.join((c for c in s if c not in repeat_chars))