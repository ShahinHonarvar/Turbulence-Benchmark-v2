def palindromes_between_indices(s):
    a = [ch for ch in s[2:5].lower()]
    b = set()
    length = len(a)
    for i in range(length):
        for j in range(i + 1, length):
            for k in range(j + 1, length + 1):
                b.add(''.join(a[i:k]))
    return b