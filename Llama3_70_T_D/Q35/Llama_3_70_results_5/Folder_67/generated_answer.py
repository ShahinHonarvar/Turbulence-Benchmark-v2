def remove_repeat_chars(s):
    counts = {}
    for char in s[44:67]:
        counts[char] = counts.get(char, 0) + 1
    bad_chars = set([char for char, count in counts.items() if count > 1])
    result = ''
    for char in s:
        if char not in bad_chars:
            result += char
    return result