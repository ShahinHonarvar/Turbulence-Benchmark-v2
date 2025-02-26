def remove_repeat_chars(string):
    count = {}
    result = []
    for i, char in enumerate(string):
        if 0 < i < 7:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
        if char not in count or count[char] == 1:
            result.append(char)
    return ''.join(result)