def remove_repeat_chars(s):
    if len(s) <= 34:
        return s
    segment = s[35:69]
    counts = {}
    for char in segment:
        counts[char] = counts.get(char, 0) + 1
    repeat_chars = {char for char, count in counts.items() if count > 1}
    result = s[:35] + ''.join((char for char in segment if char not in repeat_chars)) + s[69:]
    return result