def remove_repeat_chars(s):
    substring = s[26:80]
    char_count = {}
    for char in substring:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    chars_to_remove = {char for char, count in char_count.items() if count > 1}
    result = [char for char in s if char not in chars_to_remove or s.index(char) <= 25 or s.index(char) >= 80]
    return ''.join(result)