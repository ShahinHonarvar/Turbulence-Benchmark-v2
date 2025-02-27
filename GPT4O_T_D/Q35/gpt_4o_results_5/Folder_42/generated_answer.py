def remove_repeat_chars(s):
    sub_str = s[19:60]
    char_count = {}
    for char in sub_str:
        char_count[char] = char_count.get(char, 0) + 1
    result = []
    for char in s:
        if char in char_count and char_count[char] > 1 and (18 < s.index(char) < 60):
            continue
        result.append(char)
    return ''.join(result)