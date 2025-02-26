def remove_repeat_chars(s):
    target_substring = s[47:91]
    char_counts = {}
    for char in target_substring:
        char_counts[char] = char_counts.get(char, 0) + 1
    repeated_chars = {char for char, count in char_counts.items() if count > 1}
    result = []
    for char in s:
        if char not in repeated_chars:
            result.append(char)
    return ''.join(result)