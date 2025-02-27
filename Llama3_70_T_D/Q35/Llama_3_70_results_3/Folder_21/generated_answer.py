def remove_repeat_chars(s):
    count = {}
    for i in range(462, 995):
        if s[i] in count:
            count[s[i]] += 1
        else:
            count[s[i]] = 1
    repeat_chars = set([char for char, freq in count.items() if freq > 1])
    return ''.join([c for i, c in enumerate(s) if c not in repeat_chars])