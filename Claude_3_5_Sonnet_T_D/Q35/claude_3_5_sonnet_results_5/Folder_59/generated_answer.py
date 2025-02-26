def remove_repeat_chars(s):
    count = {}
    result = []
    for i, char in enumerate(s):
        if 0 < i < 10:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
        result.append(char)
    return ''.join([char for char in result if char not in count or count[char] == 1])