def remove_repeat_chars(s):
    count = {}
    for i in range(42, 87):
        if s[i] in count:
            count[s[i]] += 1
        else:
            count[s[i]] = 1
    remove = [char for char, freq in count.items() if freq > 1]
    return ''.join([char for char in s if char not in remove])