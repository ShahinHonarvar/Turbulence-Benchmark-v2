def remove_repeat_chars(s):
    target_substring = s[20:32]
    char_counts = {}
    for char in target_substring:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    chars_to_remove = {char for char, count in char_counts.items() if count > 1}
    return ''.join((char for char in s if char not in chars_to_remove or s.index(char) <= 19 or s.index(char) >= 32))