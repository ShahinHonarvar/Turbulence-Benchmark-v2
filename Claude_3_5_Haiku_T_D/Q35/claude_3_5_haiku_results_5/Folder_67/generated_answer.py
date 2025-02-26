def remove_repeat_chars(s):
    segment = s[45:67]
    repeated_chars = set()
    for char in segment:
        if segment.count(char) > 1 and char not in repeated_chars:
            repeated_chars.add(char)
    result = ''.join((char for char in s if char not in repeated_chars or s.index(char) < 45 or s.index(char) >= 67))
    return result