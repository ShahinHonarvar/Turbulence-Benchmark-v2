def remove_repeat_chars(s):
    count = {}
    for i in range(330, 543):
        if s[i] not in count:
            count[s[i]] = 0
        count[s[i]] += 1
    to_remove = {char for char, freq in count.items() if freq > 1}
    return ''.join((char for char in s if char not in to_remove))