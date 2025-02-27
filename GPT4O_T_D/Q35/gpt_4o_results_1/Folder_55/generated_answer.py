def remove_repeat_chars(s):
    if len(s) <= 10:
        return s
    check_slice = s[11:100]
    char_counts = {}
    for char in check_slice:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    chars_to_remove = {char for char, count in char_counts.items() if count > 1}
    result = []
    for char in s:
        if char not in chars_to_remove:
            result.append(char)
    return ''.join(result)