def remove_repeat_chars(s):
    if len(s) <= 50:
        return s
    start, end = (50, 74)
    substring = s[start:end]
    char_count = {}
    for char in substring:
        char_count[char] = char_count.get(char, 0) + 1
    to_remove = {char for char, count in char_count.items() if count > 1}
    result = [char for char in s if char not in to_remove]
    return ''.join(result)