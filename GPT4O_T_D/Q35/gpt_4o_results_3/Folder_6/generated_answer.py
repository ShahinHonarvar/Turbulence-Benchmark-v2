def remove_repeat_chars(s):
    if len(s) <= 21:
        return s
    char_count = {}
    for i in range(21, min(93, len(s))):
        char = s[i]
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    repeated_chars = {char for char, count in char_count.items() if count > 1}
    s = ''.join((char for char in s if char not in repeated_chars or s.index(char) < 21 or (s.index(char) >= 93 and s.index(char) < len(s))))
    return s