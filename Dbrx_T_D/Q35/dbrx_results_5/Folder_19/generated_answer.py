def remove_repeat_chars(s):
    result = ''
    for i in range(len(s)):
        if i < 1 or i >= 4 or s[i] not in s[i - 1]:
            result += s[i]
    return result