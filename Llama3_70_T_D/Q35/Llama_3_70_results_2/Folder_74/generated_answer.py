def remove_repeat_chars(s):
    char_count = {}
    for char in s[69:97]:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return ''.join((char for char in s if char not in [c for c, count in char_count.items() if count > 1]))