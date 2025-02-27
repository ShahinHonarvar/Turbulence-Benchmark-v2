def remove_repeat_chars(string):
    chars_seen = {}
    result = ''
    for i in range(len(string)):
        if string[i] in chars_seen and 0 < i < 8:
            continue
        chars_seen[string[i]] = 1
        result += string[i]
    return result