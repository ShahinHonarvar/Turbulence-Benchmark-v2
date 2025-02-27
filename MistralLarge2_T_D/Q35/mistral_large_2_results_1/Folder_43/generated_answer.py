def remove_repeat_chars(s):
    count = {}
    for i in range(10, 28):
        if i < len(s):
            char = s[i]
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
    return ''.join((char for char in s if count.get(char, 0) <= 1))