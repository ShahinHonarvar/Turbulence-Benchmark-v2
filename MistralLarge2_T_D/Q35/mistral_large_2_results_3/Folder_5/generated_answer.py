def remove_repeat_chars(s):
    count = {}
    for char in s[2:8]:
        count[char] = count.get(char, 0) + 1
    for char in count:
        if count[char] > 1:
            s = s.replace(char, '')
    return s