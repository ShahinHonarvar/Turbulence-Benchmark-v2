def remove_repeat_chars(s):
    seen = set()
    repeats = set()
    for i in range(1, 9):
        if s[i] in seen:
            repeats.add(s[i])
        seen.add(s[i])
    return ''.join((char for char in s if char not in repeats))