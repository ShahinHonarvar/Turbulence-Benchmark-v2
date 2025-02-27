def remove_repeat_chars(s):
    char_count = {}
    for i in range(17, 88):
        char_count[s[i]] = char_count.get(s[i], 0) + 1
    repeat_chars = [ch for ch, count in char_count.items() if count > 1]
    for ch in repeat_chars:
        s = s.replace(ch, '')
    return s