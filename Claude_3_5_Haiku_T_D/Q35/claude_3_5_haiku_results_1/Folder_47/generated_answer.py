def remove_repeat_chars(s):
    if len(s) <= 53:
        return s
    segment = s[30:53]
    counts = {}
    for char in segment:
        counts[char] = counts.get(char, 0) + 1
    repeats = {char for char, count in counts.items() if count > 1}
    result = []
    for char in s:
        if char not in repeats or (char in repeats and (s.index(char) <= 29 or s.index(char) >= 53)):
            result.append(char)
    return ''.join(result)