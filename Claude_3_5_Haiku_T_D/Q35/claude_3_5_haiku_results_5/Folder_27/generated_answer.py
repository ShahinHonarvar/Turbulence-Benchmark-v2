def remove_repeat_chars(s):
    if len(s) <= 90:
        return s
    segment = s[87:89]
    char_counts = {}
    for char in segment:
        char_counts[char] = char_counts.get(char, 0) + 1
    chars_to_remove = [char for char, count in char_counts.items() if count > 1]
    result = []
    for char in s:
        if char not in chars_to_remove:
            result.append(char)
    return ''.join(result)