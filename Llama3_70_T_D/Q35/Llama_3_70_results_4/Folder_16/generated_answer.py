def remove_repeat_chars(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    result = ''
    for char in s:
        if char in ['a', 'b', 'c', 'd', 'e', 'f', 'g'] and char_count[char] > 1:
            continue
        result += char
    return result