def remove_repeat_chars(s):
    target_substring = s[39:81]
    char_counts = {}
    for char in target_substring:
        char_counts[char] = char_counts.get(char, 0) + 1
    repeating_chars = set((char for char, count in char_counts.items() if count > 1))
    result = ''
    for i, char in enumerate(s):
        if i < 38 or i > 81 or char not in repeating_chars:
            result += char
    return result