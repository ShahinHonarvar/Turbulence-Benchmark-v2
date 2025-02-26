def remove_repeat_chars(s):
    substring = s[17:87]
    char_counts = {}
    for char in substring:
        char_counts[char] = char_counts.get(char, 0) + 1
    repeats = {char for char, count in char_counts.items() if count > 1}
    result = ''.join((char for char in s if char not in repeats or s.index(char) < 17 or s.index(char) >= 87))
    return result