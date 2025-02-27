def remove_repeat_chars(s):
    l = list(s)
    freq = {}
    for i in range(4):
        if l[i] in freq:
            freq[l[i]] += 1
        else:
            freq[l[i]] = 1
    repeat_chars = [k for k, v in freq.items() if v > 1]
    for c in repeat_chars:
        l = [x for x in l if x != c]
    return ''.join(l)