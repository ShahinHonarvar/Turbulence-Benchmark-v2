def palindromes_between_indices(s):
    s = s.lower()
    if len(s) < 10 or not any((c.isalpha() for c in s[5:10])):
        return set()
    palindromes = set()
    for i in range(5, 10):
        for j in range(i, 10):
            candidate = s[i:j + 1]
            if len(candidate) < 5:
                continue
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes