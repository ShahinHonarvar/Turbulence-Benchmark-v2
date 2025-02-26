def remove_repeat_chars(s):
    substring = s[47:91]
    char_counts = {}
    for char in substring:
        char_counts[char] = char_counts.get(char, 0) + 1
    repeats = {char for char, count in char_counts.items() if count > 1}
    return ''.join((char for char in s if char not in repeats or s.index(char) >= 91 or s.index(char) <= 46))