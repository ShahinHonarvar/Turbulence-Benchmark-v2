def remove_repeat_chars(string):
    chars = {}
    result = []
    for i, char in enumerate(string):
        if i in range(29, 53):
            if char not in chars or chars[char] != i:
                result.append(char)
                chars[char] = i
    return ''.join(result)