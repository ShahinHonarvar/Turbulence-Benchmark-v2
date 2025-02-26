def remove_repeat_chars(s):
    if len(s) <= 45:
        return s
    subset = s[45:78]
    repeats = set((char for char in subset if subset.count(char) > 1))
    result = ''.join((char for char in s if char not in repeats or s.index(char) < 45 or s.index(char) >= 78))
    return result