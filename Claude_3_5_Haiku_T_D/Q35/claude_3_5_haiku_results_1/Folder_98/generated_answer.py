def remove_repeat_chars(s):
    char_count = {}
    repeat_chars = set()
    for i in range(1, 7):
        if s[i] in char_count:
            repeat_chars.add(s[i])
        else:
            char_count[s[i]] = 1
    return ''.join((char for char in s if char not in repeat_chars))