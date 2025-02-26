def remove_repeat_chars(s):
    if len(s) <= 4:
        return s
    substring = s[4:-1]
    char_counts = {}
    for char in substring:
        char_counts[char] = char_counts.get(char, 0) + 1
    repeated_chars = {char for char, count in char_counts.items() if count > 1}
    result = s[0:4] + ''.join((char for char in substring if char not in repeated_chars)) + s[-1]
    return result