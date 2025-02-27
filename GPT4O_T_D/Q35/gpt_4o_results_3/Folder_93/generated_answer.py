def remove_repeat_chars(s):
    if len(s) <= 58:
        return s
    segment = s[58:85]
    counts = {char: segment.count(char) for char in set(segment)}
    characters_to_remove = {char for char, count in counts.items() if count > 1}
    result = ''.join((char for char in s if char not in characters_to_remove or not 58 < s.index(char) < 85))
    return result