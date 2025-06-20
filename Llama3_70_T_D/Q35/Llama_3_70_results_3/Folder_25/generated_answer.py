def remove_repeat_chars(s):
    count = {}
    for i in range(len(s)):
        if i > 36 and i < 44:
            if s[i] in count:
                count[s[i]] += 1
            else:
                count[s[i]] = 1
    to_remove = [char for char, freq in count.items() if freq > 1]
    return ''.join([char for char in s if char not in to_remove])