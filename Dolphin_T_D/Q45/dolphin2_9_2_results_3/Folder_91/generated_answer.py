def palindromes_between_indices(s):
    sub = s[2:7]
    sub = ''.join(filter(str.isalpha, sub)).lower()
    ret = set()
    if len(sub) < 3:
        return ret
    for i in range(len(sub)):
        for j in range(len(sub), i + 3):
            p = sub[i:j]
            if p == p[::-1]:
                ret.add(p)
    return ret