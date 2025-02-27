def remove_repeat_chars(s):
    char_count = {}
    for char in s:
        if 32 < ord(char) < 99:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    result = ''
    for char in s:
        if 32 < ord(char) < 99 and char_count[char] > 1:
            continue
        result += char
    return result