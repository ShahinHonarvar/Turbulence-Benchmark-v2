def palindromes_between_indices(s):
    s = s[6:10].lower()
    letters = set((c for c in s if c.isalpha()))
    palindromes = set()
    for c1 in letters:
        for c2 in letters:
            for c3 in letters:
                for c4 in letters:
                    for c5 in letters:
                        palindrome = c1 + c2 + c3 + c4 + c5
                        if palindrome == palindrome[::-1]:
                            palindromes.add(palindrome)
    return palindromes