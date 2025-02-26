def remove_repeat_chars(s):
    if len(s) <= 90:
        return s
    substring = s[87:89]
    char_counts = {}
    for char in substring:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    repeats = [char for char, count in char_counts.items() if count > 1]
    result = ''.join((char for char in s if char not in repeats))
    return result