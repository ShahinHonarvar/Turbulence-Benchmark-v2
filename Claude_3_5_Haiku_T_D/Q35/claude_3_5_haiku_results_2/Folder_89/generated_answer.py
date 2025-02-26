def remove_repeat_chars(s):
    if len(s) <= 56:
        return s
    segment = s[56:84]
    to_remove = set()
    for i in range(len(segment)):
        if segment[i] in segment[i + 1:]:
            to_remove.add(segment[i])
    result = ''.join((char for char in s if char not in to_remove or s.index(char) < 56 or s.index(char) >= 84))
    return result