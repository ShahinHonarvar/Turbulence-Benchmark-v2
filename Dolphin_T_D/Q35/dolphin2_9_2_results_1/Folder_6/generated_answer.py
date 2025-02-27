def remove_repeat_chars(s):
    char_count = {char: 0 for char in s}
    for i in range(20, 93):
        if char_count[s[i]] == 1:
            s = s[:i] + s[i + 1:]
            i -= 1
        else:
            char_count[s[i]] += 1
    return s