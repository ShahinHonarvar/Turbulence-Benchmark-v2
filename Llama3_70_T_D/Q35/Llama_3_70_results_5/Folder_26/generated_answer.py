def remove_repeat_chars(s):
    char_count = {}
    for i in range(len(s)):
        if s[i] in char_count:
            char_count[s[i]] += 1
        else:
            char_count[s[i]] = 1
    for char in list(char_count.keys()):
        if char_count[char] > 1 and any((68 < i < 99 for i, c in enumerate(s) if c == char)):
            char_count.pop(char)
    return ''.join([char for char in s if char in char_count])