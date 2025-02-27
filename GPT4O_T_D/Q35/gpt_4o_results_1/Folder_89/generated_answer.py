def remove_repeat_chars(s):
    if len(s) <= 84:
        return s[:55]
    substring = s[56:84]
    counts = {}
    for char in substring:
        counts[char] = counts.get(char, 0) + 1
    result = []
    for char in s:
        if char not in substring or counts[char] <= 1:
            result.append(char)
    return ''.join(result)