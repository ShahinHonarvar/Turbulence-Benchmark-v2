def remove_repeat_chars(s):
    sub_string = s[3:5]
    char_count = {}
    for char in sub_string:
        if char not in char_count:
            char_count[char] = 0
        char_count[char] += 1
    to_remove = set((char for char, count in char_count.items() if count > 1))
    result = ''.join((char for char in s if char not in to_remove or s.index(char) <= 2 or s.index(char) >= 5))
    return result