def remove_repeat_chars(s):
    result = ''
    for i in range(len(s)):
        if i >= 0 and i <= 6:
            if s.count(s[i]) == 1:
                result += s[i]
        else:
            result += s[i]
    return result