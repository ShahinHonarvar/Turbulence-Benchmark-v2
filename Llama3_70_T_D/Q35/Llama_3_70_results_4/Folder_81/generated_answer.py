def remove_repeat_chars(s):
    char_count = {}
    for char in s[20:200]:
        char_count[char] = char_count.get(char, 0) + 1
    repeat_chars = [char for char, count in char_count.items() if count > 1]
    result = ''
    for char in s:
        if char not in repeat_chars:
            result += char
    return result