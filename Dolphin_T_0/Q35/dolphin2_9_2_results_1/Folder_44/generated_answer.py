def remove_repeat_chars(s):
    count = {}
    for i in range(36, 52):
        if s[i] in count:
            count[s[i]] += 1
        else:
            count[s[i]] = 1
    chars_to_remove = [char for char, val in count.items() if val > 1]
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s