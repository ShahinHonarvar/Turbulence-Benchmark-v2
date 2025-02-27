def remove_repeat_chars(s):
    if not s or len(s) <= 31:
        return s
    char_count = {}
    for char in s[31:200]:
        char_count[char] = char_count.get(char, 0) + 1
    result = []
    for i, char in enumerate(s):
        if 31 < i < 200 and char_count.get(char, 0) > 1:
            continue
        result.append(char)
    return ''.join(result)