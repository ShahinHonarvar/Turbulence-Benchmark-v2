def remove_repeat_chars(s):
    start, end = (69, 97)
    char_count = {}
    for i in range(start, end):
        char = s[i]
        char_count[char] = char_count.get(char, 0) + 1
    to_remove = {char for char, count in char_count.items() if count > 1}
    return ''.join((char for char in s if char not in to_remove))