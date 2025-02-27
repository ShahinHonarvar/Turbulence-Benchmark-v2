def remove_repeat_chars(s):
    char_count = {}
    for i in range(49, 76):
        if i < len(s):
            char = s[i]
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    repeated_chars = {char for char, count in char_count.items() if count > 1}
    result = ''.join((char for char in s if char not in repeated_chars or s.index(char) <= 48 or s.index(char) >= 76))
    return result