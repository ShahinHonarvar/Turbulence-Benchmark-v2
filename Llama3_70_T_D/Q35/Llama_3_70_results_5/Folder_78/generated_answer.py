def remove_repeat_chars(s):
    count = {}
    for i in range(97, 123):
        count[chr(i)] = s.count(chr(i))
    result = ''
    for char in s:
        if count[char] <= 1 or (ord(char) < 62 or ord(char) > 96):
            result += char
    return result