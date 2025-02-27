def remove_repeat_chars(s):
    count = {}
    for i in range(7, 9):
        if i < len(s):
            char = s[i]
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
    result = ''.join([char for char in s if not (char in count and count[char] > 1)])
    return result