def remove_repeat_chars(s):
    count = {}
    for char in s[:3]:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    for char, freq in count.items():
        if freq > 1:
            s = s.replace(char, '')
    return s