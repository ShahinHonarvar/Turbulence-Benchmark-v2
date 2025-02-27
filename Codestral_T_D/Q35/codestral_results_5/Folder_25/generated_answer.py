def remove_repeat_chars(s):
    chars = s[37:43]
    count = {}
    for char in chars:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    repeat_chars = [char for char in count if count[char] > 1]
    for char in repeat_chars:
        s = s.replace(char, '')
    return s