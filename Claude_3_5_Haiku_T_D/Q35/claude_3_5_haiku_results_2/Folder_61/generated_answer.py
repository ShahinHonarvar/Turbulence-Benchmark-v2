def remove_repeat_chars(s):
    if len(s) <= 9:
        seen = set()
        repeats = set()
        for i in range(1, 8):
            if s[i] in seen:
                repeats.add(s[i])
            seen.add(s[i])
        return ''.join((char for char in s if char not in repeats))
    return s