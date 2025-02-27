def remove_repeat_chars(s):
    substring = s[87:89]
    for i in range(len(substring)):
        current_char = substring[i]
        if substring.count(current_char) > 1:
            s = s.replace(current_char, '')
    return s