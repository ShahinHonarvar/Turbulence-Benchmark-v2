def remove_repeat_chars(s):
    chars_to_remove = set()
    char_count = {}
    for i in range(125, 825):
        if s[i] in char_count:
            char_count[s[i]] += 1
            if char_count[s[i]] > 1:
                chars_to_remove.add(s[i])
        else:
            char_count[s[i]] = 1
    return ''.join((c for c in s if c not in chars_to_remove))