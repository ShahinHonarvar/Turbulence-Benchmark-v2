def remove_repeat_chars(s):
    count = {}
    for char in s[46:91]:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    repeat_chars = [char for char, freq in count.items() if freq > 1]
    result = []
    for char in s:
        if char not in repeat_chars:
            result.append(char)
    return ''.join(result)