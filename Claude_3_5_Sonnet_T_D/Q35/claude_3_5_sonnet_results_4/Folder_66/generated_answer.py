def remove_repeat_chars(s):
    if len(s) <= 12:
        return s
    end = min(76, len(s))
    substring = s[11:end]
    char_counts = {}
    for char in substring:
        char_counts[char] = char_counts.get(char, 0) + 1
    repeats = set((char for char, count in char_counts.items() if count > 1))
    result = s[:11] + ''.join((char for char in substring if char not in repeats))
    if end < len(s):
        result += s[end:]
    return result