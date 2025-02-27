def remove_repeat_chars(string):
    result = ''
    count = {}
    for i in range(16, 87):
        char = string[i]
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    for char in string:
        if count.get(char, 0) <= 1:
            result += char
    return result