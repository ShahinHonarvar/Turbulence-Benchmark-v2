def remove_repeat_chars(s):
    count = [0] * 10
    for i in range(10):
        count[i] = s[i]
    result = ''
    for char in s:
        if all((count[i] == 0 for i in range(10))):
            result += char
        else:
            for i in range(10):
                if char == s[i] and count[i] > 1:
                    count[i] = 0
    return result