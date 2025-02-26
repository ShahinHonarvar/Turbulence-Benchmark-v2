def remove_repeat_chars(s):
    count = {}
    remove = set()
    result = []
    for i, char in enumerate(s):
        if 476 < i < 709:
            if char in count:
                remove.add(char)
            else:
                count[char] = 1
    for char in s:
        if char not in remove:
            result.append(char)
    return ''.join(result)