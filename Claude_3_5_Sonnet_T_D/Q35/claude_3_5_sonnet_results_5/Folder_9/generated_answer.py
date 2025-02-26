def remove_repeat_chars(s):
    if len(s) <= 200:
        return s
    substring = s[80:200]
    char_count = {}
    for char in substring:
        char_count[char] = char_count.get(char, 0) + 1
    repeating_chars = {char for char, count in char_count.items() if count > 1}
    result = []
    for i, char in enumerate(s):
        if i < 80 or i >= 200 or char not in repeating_chars:
            result.append(char)
    return ''.join(result)