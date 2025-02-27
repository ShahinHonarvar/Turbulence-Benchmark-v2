def remove_repeat_chars(s):
    part_of_interest = s[14:70]
    char_counts = {}
    for char in part_of_interest:
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