def remove_repeat_chars(s):
    middle_section = s[21:35]
    char_count = {}
    for char in middle_section:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    to_remove = {char for char, count in char_count.items() if count > 1}
    result = [char for char in s if char not in to_remove or s.index(char) <= 20 or s.index(char) >= 35]
    return ''.join(result)