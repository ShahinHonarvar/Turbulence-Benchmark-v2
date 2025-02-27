def remove_repeat_chars(s):
    if len(s) <= 67:
        return s
    substring = s[45:67]
    counts = {}
    for char in substring:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return ''.join((char for char in s if counts.get(char, 0) <= 1))