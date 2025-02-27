def remove_repeat_chars(string):
    count = {}
    for i in range(11, 76):
        char = string[i]
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    result = ''
    for char in string:
        if count.get(char, 0) <= 1:
            result += char
    return result