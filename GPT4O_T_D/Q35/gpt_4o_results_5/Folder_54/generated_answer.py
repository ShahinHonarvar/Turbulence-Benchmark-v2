def remove_repeat_chars(s):
    if len(s) <= 35:
        return s
    subsequence = s[36:64]
    char_count = {}
    for char in subsequence:
        char_count[char] = char_count.get(char, 0) + 1
    repeated_chars = {char for char, count in char_count.items() if count > 1}
    result = []
    for char in s:
        if char not in repeated_chars:
            result.append(char)
    return ''.join(result)