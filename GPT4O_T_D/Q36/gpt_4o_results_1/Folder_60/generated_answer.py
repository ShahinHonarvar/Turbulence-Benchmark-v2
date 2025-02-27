def filter_chars(s):
    chars_to_remove = {chr(i) for i in range(ord('g'), ord('o'))}
    for char in s[24:83]:
        if char in chars_to_remove:
            s = s.replace(char, '')
    return s