def remove_repeat_chars(s):
    count = {}
    for char in s:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    repeat_chars = set()
    for char in s[90:97]:
        if count[char] > 1:
            repeat_chars.add(char)
    result = ''
    for char in s:
        if char not in repeat_chars:
            result += char
    return result