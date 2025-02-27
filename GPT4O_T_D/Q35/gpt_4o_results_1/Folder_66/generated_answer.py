def remove_repeat_chars(s):
    substring = s[12:76]
    char_counts = {}
    for char in substring:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    to_remove = {char for char, count in char_counts.items() if count > 1}
    result = ''.join((char for char in s if char not in to_remove or s.index(char) <= 11 or s.index(char) >= 76))
    return result