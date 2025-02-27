def remove_repeat_chars(s):
    substring = s[11:76]
    char_count = {}
    for char in substring:
        char_count[char] = char_count.get(char, 0) + 1
    chars_to_remove = {char for char, count in char_count.items() if count > 1}
    result = []
    for char in s:
        if char in chars_to_remove and 11 < s.index(char) < 76:
            continue
        result.append(char)
    return ''.join(result)