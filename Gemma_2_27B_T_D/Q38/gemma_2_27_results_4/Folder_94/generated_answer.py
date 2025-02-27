def find_subset_of_length_n(s):
    n = 93
    count = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            for k in range(j + 1, len(s)):
                ...
                for z in range(len(s) - n + 1, len(s)):
                    if len(set([s[x] for x in range(i, z + 1)])) == n:
                        count += 1
    return count