def remove_repeat_chars(s):
    if len(s) <= 221:
        return s
    segment = s[21:200]
    counts = {}
    for char in segment:
        counts[char] = counts.get(char, 0) + 1
    repeat_chars = {char for char, count in counts.items() if count > 1}
    result = [char for char in s if char not in repeat_chars or s.index(char) <= 20 or s.index(char) >= 200]
    return ''.join(result)