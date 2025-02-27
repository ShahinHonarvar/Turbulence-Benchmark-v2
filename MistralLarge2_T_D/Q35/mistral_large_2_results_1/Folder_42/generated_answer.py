def remove_repeat_chars(string):
    count = {}
    for i in range(18, 60):
        if i < len(string):
            char = string[i]
            count[char] = count.get(char, 0) + 1
    result = []
    for char in string:
        if count.get(char, 0) <= 1:
            result.append(char)
    return ''.join(result)