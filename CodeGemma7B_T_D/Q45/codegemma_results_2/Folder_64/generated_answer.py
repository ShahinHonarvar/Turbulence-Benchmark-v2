def palindromes_between_indices(s):
    palindromes = set()
    for i in range(4, 10):
        for j in range(i + 1, 10):
            for k in range(j + 1, 10):
                for l in range(k + 1, 10):
                    for m in range(l + 1, 10):
                        letters = [c for c in s[i:m + 1] if c.isalpha()]
                        palindrome = ''.join(sorted(letters, key=str.lower))
                        palindromes.add(palindrome)
    return palindromes