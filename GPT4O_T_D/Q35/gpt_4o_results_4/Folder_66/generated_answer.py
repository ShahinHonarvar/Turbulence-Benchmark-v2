def remove_repeat_chars(s):
    if len(s) <= 11:
        return s
    start_index = 12
    end_index = min(len(s), 76)
    substring = s[start_index:end_index]
    char_count = {}
    for char in substring:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    chars_to_remove = {char for char, count in char_count.items() if count > 1}
    result = []
    for i, char in enumerate(s):
        if start_index <= i < end_index and char in chars_to_remove:
            continue
        result.append(char)
    return ''.join(result)