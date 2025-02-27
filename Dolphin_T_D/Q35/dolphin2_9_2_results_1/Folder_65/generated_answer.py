def remove_repeat_chars(s):
    char_count = {}
    for i in range(51, 76):
        if s[i] in char_count:
            char_count[s[i]] += 1
        else:
            char_count[s[i]] = 1
    chars_to_remove = [char for char, count in char_count.items() if count > 1]
    new_s = ''
    for ch in s:
        if ch not in chars_to_remove:
            new_s += ch
    return new_s