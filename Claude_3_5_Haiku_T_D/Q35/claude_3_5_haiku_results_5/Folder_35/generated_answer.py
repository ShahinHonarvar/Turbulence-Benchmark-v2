def remove_repeat_chars(s):
    if len(s) <= 85:
        return s
    substring = s[78:84]
    char_counts = {}
    repeat_chars = set()
    for char in substring:
        char_counts[char] = char_counts.get(char, 0) + 1
        if char_counts[char] > 1:
            repeat_chars.add(char)
    result = ''.join((char for char in s if char not in repeat_chars or s.index(char) <= 77 or s.index(char) >= 84))
    return result