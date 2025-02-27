def remove_repeat_chars(s):
    chars_to_remove = []
    for i in range(86, 91):
        if s.count(s[i]) > 1:
            chars_to_remove.append(s[i])
    new_s = ''
    for i in s:
        if i not in chars_to_remove:
            new_s += i
    return new_s