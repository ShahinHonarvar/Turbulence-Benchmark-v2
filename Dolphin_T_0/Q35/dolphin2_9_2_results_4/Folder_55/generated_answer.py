def remove_repeat_chars(s):
    chars_between_10_and_100 = s[10:100]
    char_counts = {}
    for char in chars_between_10_and_100:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    repeat_chars = [char for char, count in char_counts.items() if count > 1]
    for char in repeat_chars:
        s = s.replace(char, '')
    return s