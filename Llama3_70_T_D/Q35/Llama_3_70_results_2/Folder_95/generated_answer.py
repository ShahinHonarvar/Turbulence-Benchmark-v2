def remove_repeat_chars(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    repeat_chars = [char for char, count in char_count.items() if count > 1 and 32 < ord(char) < 99]
    result = ''
    for char in s:
        if char not in repeat_chars:
            result += char
    return result