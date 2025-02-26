def remove_repeat_chars(s):
    target_substring = s[46:91]
    char_count = {}
    for char in target_substring:
        char_count[char] = char_count.get(char, 0) + 1
    repeated_chars = {char for char, count in char_count.items() if count > 1}
    result = ''
    for i, char in enumerate(s):
        if i < 46 or i >= 91 or char not in repeated_chars:
            result += char
    return result