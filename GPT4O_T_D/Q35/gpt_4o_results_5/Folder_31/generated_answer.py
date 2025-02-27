def remove_repeat_chars(s):
    substring = s[34:78]
    char_counts = {}
    for char in substring:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    repeated_chars = {char for char, count in char_counts.items() if count > 1}
    result = [char for char in s if char not in repeated_chars]
    return ''.join(result)