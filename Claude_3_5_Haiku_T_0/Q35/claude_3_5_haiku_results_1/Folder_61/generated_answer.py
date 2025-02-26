def remove_repeat_chars(s):
    if len(s) <= 9:
        char_count = {}
        for i in range(1, 8):
            if s[i] in char_count:
                char_count[s[i]] += 1
            else:
                char_count[s[i]] = 1
        repeated_chars = [char for char, count in char_count.items() if count > 1]
        return ''.join((char for char in s if char not in repeated_chars))
    return s