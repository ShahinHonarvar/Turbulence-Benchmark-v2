def palindromes_between_indices(s):
    s = s.lower()
    subset = set(s[1:5])
    subset = ''.join(sorted(subset))
    if len(subset) < 5:
        return set()
    else:
        palindromes = set()
        for i in range(len(subset) // 2 + 1):
            palindrome = subset[:i] + subset[i - 1::-1]
            palindromes.add(palindrome)
        return palindromes