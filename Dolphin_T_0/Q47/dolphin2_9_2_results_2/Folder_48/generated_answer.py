def palindromes_of_specific_lengths(s):
    s = s[155:283]
    palindromes = set()
    for size in range(104, 121):
        for i in range(len(s) - size + 1):
            sub = s[i:i + size]
            if sub.lower() == sub.lower()[::-1]:
                palindromes.add(sub)
    return palindromes