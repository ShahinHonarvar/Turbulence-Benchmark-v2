def remove_repeat_chars(s):
    if len(s) <= 90:
        return s
    char_count = {}
    for i in range(91, min(len(s) - 1, 200)):
        char = s[i]
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    to_remove = {char for char, count in char_count.items() if count > 1}
    return ''.join((char for char in s if char not in to_remove))