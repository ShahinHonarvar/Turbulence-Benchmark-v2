def remove_repeat_chars(s):
    char_count = {}
    for char in s:
        if 32 < ord(char) < 99:
            char_count[char] = char_count.get(char, 0) + 1
    result = []
    for char in s:
        if 32 < ord(char) < 99 and char_count[char] == 1 or not 32 < ord(char) < 99:
            result.append(char)
    return ''.join(result)