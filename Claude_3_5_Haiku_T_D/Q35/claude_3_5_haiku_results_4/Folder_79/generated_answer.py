def remove_repeat_chars(s):
    if len(s) <= 2:
        return s
    slice_str = s[1:7]
    repeats = set((char for char in slice_str if slice_str.count(char) > 1))
    result = ''.join((char for char in s if char not in repeats or s.index(char) < 1 or s.index(char) >= 7))
    return result