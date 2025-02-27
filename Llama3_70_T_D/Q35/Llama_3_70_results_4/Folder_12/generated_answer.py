def remove_repeat_chars(s):
    count = {}
    for i in range(16, 87):
        if s[i] in count:
            count[s[i]] += 1
        else:
            count[s[i]] = 1
    repeat_chars = set([char for char in count if count[char] > 1])
    return ''.join([char for char in s if char not in repeat_chars])