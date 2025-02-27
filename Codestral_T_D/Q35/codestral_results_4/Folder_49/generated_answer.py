def remove_repeat_chars(s):
    char_count = {}
    for i in range(90, 200):
        if i < len(s):
            char_count[s[i]] = char_count.get(s[i], 0) + 1
    return ''.join((char for char in s if char_count.get(char, 0) <= 1))