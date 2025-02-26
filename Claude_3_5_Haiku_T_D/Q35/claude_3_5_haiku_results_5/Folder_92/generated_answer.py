def remove_repeat_chars(s):
    if len(s) <= 2:
        return s
    substring = s[1:3]
    counts = {}
    for char in substring:
        counts[char] = counts.get(char, 0) + 1
    repeated_chars = [char for char, count in counts.items() if count > 1]
    return ''.join((char for char in s if char not in repeated_chars))