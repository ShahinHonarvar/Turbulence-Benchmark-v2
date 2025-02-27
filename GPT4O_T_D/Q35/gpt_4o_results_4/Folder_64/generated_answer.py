def remove_repeat_chars(s):
    substring = s[1:5]
    char_count = {}
    for char in substring:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    to_remove = set((char for char, count in char_count.items() if count > 1))
    return ''.join((char for char in s if char not in to_remove))