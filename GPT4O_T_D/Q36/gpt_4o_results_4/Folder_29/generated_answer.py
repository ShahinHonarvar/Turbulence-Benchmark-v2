def filter_chars(s):
    s = list(s)
    for i in range(47, 68):
        if i < len(s) and 'H' < s[i] < 's':
            char_to_remove = s[i]
            s = [char for char in s if char != char_to_remove]
    return ''.join(s)