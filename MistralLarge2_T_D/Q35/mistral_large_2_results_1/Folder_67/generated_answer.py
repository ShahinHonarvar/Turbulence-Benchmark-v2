def remove_repeat_chars(s):
    substring = s[44:67]
    counts = {}
    for char in substring:
        counts[char] = counts.get(char, 0) + 1
    for char, count in counts.items():
        if count > 1:
            s = s.replace(char, '')
    return s