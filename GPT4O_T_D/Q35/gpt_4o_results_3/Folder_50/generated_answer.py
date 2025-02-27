def remove_repeat_chars(s):
    substring = s[14:76]
    char_counts = {}
    for char in substring:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    remove_chars = {char for char, count in char_counts.items() if count > 1}
    result = ''.join((char for char in s if char not in remove_chars or s.index(char) <= 13 or s.index(char) >= 76))
    return result