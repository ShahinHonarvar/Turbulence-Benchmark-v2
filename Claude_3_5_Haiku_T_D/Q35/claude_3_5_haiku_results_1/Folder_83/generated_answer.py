def remove_repeat_chars(string):
    if len(string) <= 201:
        return string
    substring = string[101:200]
    char_counts = {}
    for char in substring:
        char_counts[char] = char_counts.get(char, 0) + 1
    repeated_chars = {char for char, count in char_counts.items() if count > 1}
    result = []
    used_chars = set()
    for char in string:
        if char in repeated_chars and char not in used_chars:
            used_chars.add(char)
        else:
            result.append(char)
    return ''.join(result)