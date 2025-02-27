def remove_repeat_chars(s):
    count = {}
    for i in range(2, 8):
        if i < len(s):
            if s[i] in count:
                count[s[i]] += 1
            else:
                count[s[i]] = 1
    repeat_chars = [char for char, freq in count.items() if freq > 1]
    new_s = ''
    for char in s:
        if char not in repeat_chars:
            new_s += char
    return new_s