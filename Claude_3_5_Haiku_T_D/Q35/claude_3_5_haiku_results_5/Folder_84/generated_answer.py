def remove_repeat_chars(s):
    char_counts = {}
    for i in range(33, 44):
        if i < len(s):
            char = s[i]
            char_counts[char] = char_counts.get(char, 0) + 1
    repeated_chars = {char for char, count in char_counts.items() if count > 1}
    result = []
    for char in s:
        if char not in repeated_chars:
            result.append(char)
    return ''.join(result)