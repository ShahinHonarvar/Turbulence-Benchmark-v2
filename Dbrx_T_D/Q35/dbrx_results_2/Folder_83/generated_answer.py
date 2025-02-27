def remove_repeat_chars(s):
    char_count = {}
    for i in range(len(s)):
        if i >= 100 and i < 200 and (s[i] in char_count):
            continue
        if s[i] not in char_count:
            char_count[s[i]] = 0
        char_count[s[i]] += 1
    result = ''
    for char in s:
        if char in char_count and char_count[char] == 1:
            result += char
    return result