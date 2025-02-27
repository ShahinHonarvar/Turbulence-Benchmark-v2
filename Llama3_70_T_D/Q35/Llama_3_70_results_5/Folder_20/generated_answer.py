def remove_repeat_chars(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    result = []
    for char in s:
        if char_count[char] > 1 and 27 < ord(char) < 96:
            continue
        else:
            result.append(char)
    return ''.join(result)