def remove_repeat_chars(s):
    substring = s[451:905]
    char_count = {}
    for char in substring:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    repeat_chars = {char for char, count in char_count.items() if count > 1}
    result = [char for i, char in enumerate(s) if char not in repeat_chars or i <= 450 or i >= 905]
    return ''.join(result)