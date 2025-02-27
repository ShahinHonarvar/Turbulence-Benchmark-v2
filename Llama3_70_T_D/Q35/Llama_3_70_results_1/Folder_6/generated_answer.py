def remove_repeat_chars(s):
    char_count = {}
    for i in range(20, 93):
        if s[i] in char_count:
            char_count[s[i]] += 1
        else:
            char_count[s[i]] = 1
    repeat_chars = [char for char in char_count if char_count[char] > 1]
    result = []
    for char in s:
        if char not in repeat_chars:
            result.append(char)
    return ''.join(result)