def all_substring_of_size_n(s):
    res = []
    for i in range(len(s) - 143):
        substrings = set()
        for j in range(i, i + 144):
            substrings.add(s[j])
        if len(substrings) == 144:
            res.append(''.join(substrings))
    return res