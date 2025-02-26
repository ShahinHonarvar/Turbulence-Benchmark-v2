def remove_repeat_chars(s):
    char_count = {}
    to_remove = set()
    for i in range(1, 7):
        if s[i] in char_count:
            to_remove.add(s[i])
        else:
            char_count[s[i]] = 1
    return ''.join((char for char in s if char not in to_remove))