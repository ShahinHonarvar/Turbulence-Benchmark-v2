def remove_repeat_chars(s):
    start, end = (13, 91)
    char_count = {}
    for i in range(start, end):
        if i < len(s):
            char_count[s[i]] = char_count.get(s[i], 0) + 1
    to_remove = {char for char, count in char_count.items() if count > 1}
    return ''.join((char for char in s if char not in to_remove))