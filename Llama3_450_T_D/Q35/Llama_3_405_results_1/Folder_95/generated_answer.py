def remove_repeat_chars(s):
    char_count = {}
    for char in s:
        if ord(char) > 32 and ord(char) < 99:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    result = ''
    for char in s:
        if ord(char) <= 32 or ord(char) >= 99 or char_count[char] == 1:
            result += char
    return result