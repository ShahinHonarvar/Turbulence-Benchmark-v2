def remove_repeat_chars(s):
    count = {}
    for i in range(51, 76):
        if i < len(s):
            char = s[i]
            count[char] = count.get(char, 0) + 1
    result = ''.join((char for char in s if count.get(char, 0) <= 1))
    return result