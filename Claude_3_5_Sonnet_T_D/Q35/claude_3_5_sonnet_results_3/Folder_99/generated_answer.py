def remove_repeat_chars(s):
    target_substring = s[451:905]
    char_count = {}
    for char in target_substring:
        char_count[char] = char_count.get(char, 0) + 1
    repeating_chars = {char for char, count in char_count.items() if count > 1}
    result = []
    for char in s:
        if char not in repeating_chars:
            result.append(char)
    return ''.join(result)