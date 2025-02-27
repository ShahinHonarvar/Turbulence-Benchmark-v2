def remove_repeat_chars(s):
    count = {}
    for i in range(44, 78):
        if s[i] in count:
            count[s[i]] += 1
        else:
            count[s[i]] = 1
    repeat_chars = [char for char, freq in count.items() if freq > 1]
    result = []
    for char in s:
        if char not in repeat_chars:
            result.append(char)
    return ''.join(result)