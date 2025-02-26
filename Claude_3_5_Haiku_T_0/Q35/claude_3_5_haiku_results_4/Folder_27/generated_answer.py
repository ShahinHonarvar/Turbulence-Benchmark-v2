def remove_repeat_chars(s):
    if len(s) <= 90:
        return s
    substring = s[87:89]
    char_counts = {}
    for char in substring:
        char_counts[char] = char_counts.get(char, 0) + 1
    repeated_chars = [char for char, count in char_counts.items() if count > 1]
    result = ''.join((char for char in s if char not in repeated_chars))
    return result