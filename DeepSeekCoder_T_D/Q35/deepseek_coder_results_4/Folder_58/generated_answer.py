def remove_repeat_chars(s):
    if len(s) <= 103:
        return s
    start = 103
    end = min(802, len(s))
    chars_to_remove = set()
    char_count = {}
    for char in s[start:end]:
        if char in char_count:
            chars_to_remove.add(char)
        char_count[char] = char_count.get(char, 0) + 1
    result = []
    for char in s:
        if char not in chars_to_remove:
            result.append(char)
    return ''.join(result)