def remove_repeat_chars(string):
    count = {}
    for i in range(77, 84):
        if i >= len(string):
            break
        char = string[i]
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    for char in count:
        if count[char] > 1:
            string = string.replace(char, '')
    return string