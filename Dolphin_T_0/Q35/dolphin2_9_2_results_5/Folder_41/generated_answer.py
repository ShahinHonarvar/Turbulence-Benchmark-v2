def remove_repeat_chars(s):
    unique_chars = set()
    for char in s[3:8]:
        if char in unique_chars:
            s = s.replace(char, '')
        else:
            unique_chars.add(char)
    return s