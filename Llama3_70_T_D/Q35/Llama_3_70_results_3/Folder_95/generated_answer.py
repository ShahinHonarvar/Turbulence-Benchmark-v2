def remove_repeat_chars(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    result = ''
    for char in s:
        if char_count[char] == 1 or (32 <= ord(char) <= 99 and char_count[char] > 1):
            result += char
        elif not 32 <= ord(char) <= 99:
            result += char
    return result