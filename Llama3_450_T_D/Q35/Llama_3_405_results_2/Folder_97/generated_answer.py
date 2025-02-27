def remove_repeat_chars(s):
    repeat_chars = set()
    char_count = {}
    for i in range(34, 69):
        if i < len(s):
            if s[i] in char_count:
                char_count[s[i]] += 1
            else:
                char_count[s[i]] = 1
            if char_count[s[i]] > 1:
                repeat_chars.add(s[i])
    return ''.join((c for c in s if c not in repeat_chars))