def remove_repeat_chars(s):
    segment = s[78:84]
    repeat_chars = set()
    for char in segment:
        if segment.count(char) > 1 and char not in repeat_chars:
            repeat_chars.add(char)
    result = ''.join((char for char in s if char not in repeat_chars or s.index(char) <= 77 or s.index(char) >= 84))
    return result