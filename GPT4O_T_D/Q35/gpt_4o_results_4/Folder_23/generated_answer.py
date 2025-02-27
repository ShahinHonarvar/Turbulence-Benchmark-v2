def remove_repeat_chars(s):
    substring = s[21:36]
    counts = {}
    for char in substring:
        counts[char] = counts.get(char, 0) + 1
    to_remove = {char for char, count in counts.items() if count > 1}
    return ''.join((char for char in s if char not in to_remove or s.index(char) >= 36 or s.index(char) <= 20))