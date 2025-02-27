def remove_repeat_chars(s):
    count = {}
    for char in s[27:96]:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    return ''.join([char for char in s if count[char] == 1])