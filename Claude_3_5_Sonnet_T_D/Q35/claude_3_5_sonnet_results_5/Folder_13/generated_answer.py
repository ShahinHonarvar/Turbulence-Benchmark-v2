def remove_repeat_chars(s):
    count = {}
    for i in range(47, 91):
        if i < len(s):
            if s[i] in count:
                count[s[i]] += 1
            else:
                count[s[i]] = 1
    repeated_chars = set((char for char, freq in count.items() if freq > 1))
    result = []
    for char in s:
        if char not in repeated_chars:
            result.append(char)
    return ''.join(result)