def remove_repeat_chars(s):
    if len(s) <= 51:
        return s
    segment = s[26:80]
    char_counts = {}
    for char in segment:
        char_counts[char] = char_counts.get(char, 0) + 1
    repeated_chars = {char for char, count in char_counts.items() if count > 1}
    result = list(s)
    for i in range(len(result)):
        if result[i] in repeated_chars and 26 < i < 80:
            result[i] = ''
    return ''.join(result)