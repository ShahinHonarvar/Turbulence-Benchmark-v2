def all_substring_of_size_n(input):
    n = 127
    curr, res = ([0] * n, [])
    charset = set()
    for char in input + '#':
        if len(charset) == n:
            res.append(''.join(curr))
            charset.remove(curr.pop(0))
        if char not in charset:
            charset.add(char)
            curr.append(char)
    return res