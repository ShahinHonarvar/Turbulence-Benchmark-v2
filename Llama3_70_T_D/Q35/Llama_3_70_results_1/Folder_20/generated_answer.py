def remove_repeat_chars(s):
    count = {}
    for char in s:
        if char not in count:
            count[char] = 1
        else:
            count[char] += 1
    result = ''
    for char in s:
        if char < chr(27) or char > chr(96):
            result += char
        elif count[char] == 1:
            result += char
    return result