def remove_repeat_chars(s):
    if not s or len(s) <= 40:
        return s
    char_count = {}
    substring = s[41:200] if len(s) > 200 else s[41:]
    for char in substring:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    chars_to_remove = {char for char, count in char_count.items() if count > 1}
    result = [char for char in s if char not in chars_to_remove or not 40 < s.index(char) < 200]
    return ''.join(result)