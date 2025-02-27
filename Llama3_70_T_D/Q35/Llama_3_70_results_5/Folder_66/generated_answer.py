def remove_repeat_chars(s):
    count = {}
    for i in range(11, 76):
        if s[i] in count:
            count[s[i]] += 1
        else:
            count[s[i]] = 1
    repeat_chars = set()
    for char, freq in count.items():
        if freq > 1:
            repeat_chars.add(char)
    result = ''
    for char in s:
        if char not in repeat_chars:
            result += char
    return result