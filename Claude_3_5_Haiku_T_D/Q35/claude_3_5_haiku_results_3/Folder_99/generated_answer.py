def remove_repeat_chars(s):
    if len(s) <= 451:
        return s
    substring = s[451:905]
    char_count = {}
    for char in substring:
        char_count[char] = char_count.get(char, 0) + 1
    repeat_chars = {char for char, count in char_count.items() if count > 1}
    result = ''.join((char for char in s if char not in repeat_chars or (char in repeat_chars and (s.index(char) < 451 or s.index(char) >= 905))))
    return result