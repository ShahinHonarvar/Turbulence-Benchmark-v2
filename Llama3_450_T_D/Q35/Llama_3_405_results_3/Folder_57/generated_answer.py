def remove_repeat_chars(s):
    chars_to_remove = set()
    char_count = {}
    for i in range(25, 80):
        if i < len(s):
            if s[i] in char_count:
                char_count[s[i]] += 1
            else:
                char_count[s[i]] = 1
            if char_count[s[i]] > 1:
                chars_to_remove.add(s[i])
    return ''.join((c for c in s if c not in chars_to_remove))