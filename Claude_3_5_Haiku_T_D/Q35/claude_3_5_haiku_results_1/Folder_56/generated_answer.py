def remove_repeat_chars(s):
    if len(s) <= 9:
        return s
    segment = s[8:9]
    counts = {}
    for char in segment:
        counts[char] = counts.get(char, 0) + 1
    repeated_chars = {char for char, count in counts.items() if count > 1}
    return ''.join((char for char in s if char not in repeated_chars or s.index(char) <= 7 or s.index(char) >= 9))