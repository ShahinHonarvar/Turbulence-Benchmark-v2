def remove_repeat_chars(s):
    target_segment = s[78:84]
    repeats = set((char for char in target_segment if target_segment.count(char) > 1))
    return ''.join((char for char in s if char not in repeats))