def remove_repeat_chars(s):
    substring = s[37:54]
    char_counts = {}
    for char in substring:
        char_counts[char] = char_counts.get(char, 0) + 1
    to_remove = {char for char, count in char_counts.items() if count > 1}
    return ''.join((char for char in s if char not in to_remove or s.index(char) <= 36 or s.index(char) >= 54))