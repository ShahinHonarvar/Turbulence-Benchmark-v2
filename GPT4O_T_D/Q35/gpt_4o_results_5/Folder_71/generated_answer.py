def remove_repeat_chars(s):
    if len(s) <= 35:
        return s
    substring = s[21:35]
    freq = {char: substring.count(char) for char in set(substring)}
    repeated_chars = {char for char, count in freq.items() if count > 1}
    return ''.join((char for char in s if char not in repeated_chars or s.index(char) <= 20 or s.index(char) >= 35))