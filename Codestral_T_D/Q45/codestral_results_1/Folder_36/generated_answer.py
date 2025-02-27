def palindromes_between_indices(s):
    s = s[5:9].lower()
    n = len(s)
    palindromes = set()
    for i in range(1 << n):
        subset = ''
        for j in range(n):
            if i & 1 << j:
                subset += s[j]
        if len(subset) >= 3 and subset == subset[::-1]:
            palindromes.add(subset)
    return palindromes