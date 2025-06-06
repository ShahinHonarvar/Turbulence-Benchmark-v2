def remove_repeat_chars(s):
    start, end = (44, 91)
    char_count = {}
    for i in range(start, end):
        if s[i] in char_count:
            char_count[s[i]] += 1
        else:
            char_count[s[i]] = 1
    to_remove = {char for char, count in char_count.items() if count > 1}
    return ''.join((char for char in s if char not in to_remove))