def remove_repeat_chars(s):
    if len(s) <= 17:
        return s
    substring = s[17:87]
    count = {}
    for char in substring:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    to_remove = {char for char, cnt in count.items() if cnt > 1}
    result = ''.join((char for char in s if char not in to_remove))
    return result