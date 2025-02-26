def remove_repeat_chars(s):
    if len(s) <= 60:
        return s
    substring = s[19:60]
    char_count = {}
    chars_to_remove = set()
    for char in substring:
        if char in char_count:
            char_count[char] += 1
            if char_count[char] > 1:
                chars_to_remove.add(char)
        else:
            char_count[char] = 1
    result = ''.join((char for char in s if char not in chars_to_remove))
    return result