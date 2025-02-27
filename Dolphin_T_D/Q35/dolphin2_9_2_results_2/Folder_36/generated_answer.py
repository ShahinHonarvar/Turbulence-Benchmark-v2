def remove_repeat_chars(s):
    char_count = {}
    result = ''
    for i in range(476, 710):
        if s[i] not in char_count:
            if s[i] in result:
                char_count[s[i]] = 1
            else:
                result += s[i]
    return result