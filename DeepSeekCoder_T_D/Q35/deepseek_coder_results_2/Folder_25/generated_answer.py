def remove_repeat_chars(s):
    start, end = (37, 43)
    sub_str = s[start:end]
    char_count = {}
    for char in sub_str:
        char_count[char] = char_count.get(char, 0) + 1
    repeated_chars = {char for char, count in char_count.items() if count > 1}
    result = []
    for char in s:
        if char not in repeated_chars:
            result.append(char)
    return ''.join(result)