def remove_repeat_chars(s):
    substring = s[45:78]
    char_count = {}
    for char in substring:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    repeated_chars = {char for char, count in char_count.items() if count > 1}
    result = ''.join((char for char in s if char not in repeated_chars or s.index(char) >= 78 or s.index(char) <= 44))
    return result