def remove_repeat_chars(s):
    substring = s[45:78]
    counts = {char: substring.count(char) for char in set(substring)}
    duplicate_chars = {char for char, count in counts.items() if count > 1}
    return ''.join((char for char in s if char not in duplicate_chars or s.index(char) <= 44 or s.index(char) >= 78))