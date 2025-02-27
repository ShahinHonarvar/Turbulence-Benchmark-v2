def remove_repeat_chars(s):
    count = {}
    for i in range(18, 60):
        if i < len(s):
            if s[i] in count:
                count[s[i]] += 1
            else:
                count[s[i]] = 1
    remove_chars = [char for char, freq in count.items() if freq > 1]
    return ''.join([char for char in s if char not in remove_chars])