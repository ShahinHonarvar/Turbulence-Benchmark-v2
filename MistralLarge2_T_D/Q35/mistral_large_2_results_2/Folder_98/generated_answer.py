def remove_repeat_chars(s):
    count = {}
    for char in s[1:7]:
        count[char] = count.get(char, 0) + 1
    result = []
    for char in s:
        if count.get(char, 0) <= 1:
            result.append(char)
    return ''.join(result)