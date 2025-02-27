def remove_repeat_chars(s):
    char_count = {}
    for i in range(38, 53):
        char = s[i]
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return ''.join((c for c in s if char_count.get(c, 0) <= 1))