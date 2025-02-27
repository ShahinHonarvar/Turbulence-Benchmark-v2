def remove_repeat_chars(s):
    if len(s) <= 80:
        return s
    substr = s[81:200] if len(s) > 200 else s[81:]
    char_count = {}
    for char in substr:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    repeating_chars = {char for char, count in char_count.items() if count > 1}
    result = []
    for char in s:
        if char not in repeating_chars:
            result.append(char)
    return ''.join(result)