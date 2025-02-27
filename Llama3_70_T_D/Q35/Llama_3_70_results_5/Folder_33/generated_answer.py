def remove_repeat_chars(s):
    s = list(s)
    char_count = {}
    for i in range(125, 825):
        if s[i] in char_count:
            char_count[s[i]] += 1
        else:
            char_count[s[i]] = 1
    repeat_chars = set([char for char, count in char_count.items() if count > 1])
    return ''.join([c for c in s if c not in repeat_chars])