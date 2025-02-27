def remove_repeat_chars(str):
    char_count = {}
    for i in range(1, 10):
        if str[i] in char_count:
            char_count[str[i]] += 1
        else:
            char_count[str[i]] = 1
    result = ''
    for char in str:
        if char in char_count and char_count[char] > 1:
            continue
        result += char
    return result