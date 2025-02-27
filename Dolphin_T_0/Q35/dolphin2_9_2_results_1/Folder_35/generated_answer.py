def remove_repeat_chars(s):
    to_remove = {}
    for i in range(77, 84):
        if s[i] in to_remove:
            to_remove[s[i]] += 1
        else:
            to_remove[s[i]] = 1
    result = ''
    for char in s:
        if char not in to_remove or to_remove[char] == 0:
            result += char
        else:
            to_remove[char] -= 1
    return result