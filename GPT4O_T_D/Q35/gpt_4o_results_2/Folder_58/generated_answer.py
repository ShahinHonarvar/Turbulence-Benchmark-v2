def remove_repeat_chars(s):
    substring = s[104:802]
    char_counts = {}
    for char in substring:
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