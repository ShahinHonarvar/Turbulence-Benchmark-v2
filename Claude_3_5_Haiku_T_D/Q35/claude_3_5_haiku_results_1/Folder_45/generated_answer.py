def remove_repeat_chars(string):
    if len(string) <= 41:
        return string
    substring = string[41:200]
    char_counts = {}
    for char in substring:
        char_counts[char] = char_counts.get(char, 0) + 1
    repeat_chars = {char for char, count in char_counts.items() if count > 1}
    result = []
    for char in string:
        if char not in repeat_chars:
            result.append(char)
    return ''.join(result)