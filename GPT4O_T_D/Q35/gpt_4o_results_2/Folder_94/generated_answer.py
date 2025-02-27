def remove_repeat_chars(s):
    sub_string = s[43:87]
    char_count = {}
    for char in sub_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    result = []
    for char in s:
        if char in char_count and char_count[char] > 1:
            continue
        result.append(char)
    return ''.join(result)