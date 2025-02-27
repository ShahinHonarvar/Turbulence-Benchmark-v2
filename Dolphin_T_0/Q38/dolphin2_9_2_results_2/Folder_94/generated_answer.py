def find_subset_of_length_n(s):
    n = 93
    return len([s1 for s1 in subset(s) if len(s1) == n])

def subset(s):
    res = []
    n = len(s)
    for i in range(1 << n):
        m = [[s[j] for j in range(n) if i & 1 << j] for i in range(n)]
        for item in m:
            if item != []:
                res.append(item)
    return res