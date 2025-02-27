def palindromes_between_indices(x):
    a = x[3:6]
    s = set([a])
    for i in range(3):
        for j in range(i + 1, 6):
            for k in range(j + 1, 6):
                for l in range(k + 1, 6):
                    for m in range(l + 1, 6):
                        a = x[i] + x[j] + x[k] + x[l] + x[m]
                        s.add(a)
    return s