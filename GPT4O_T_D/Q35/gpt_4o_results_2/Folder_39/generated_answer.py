def remove_repeat_chars(s):
    if len(s) < 92:
        return s
    target_section = s[45:91]
    char_count = {}
    for char in target_section:
        char_count[char] = char_count.get(char, 0) + 1
    result = [char for char in s if char_count.get(char, 0) <= 1 or char not in target_section]
    return ''.join(result)