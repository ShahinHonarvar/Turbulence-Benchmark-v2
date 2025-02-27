def palindromes_between_indices(s):
    letters = set((s[i].lower() for i in range(6) if s[i].isalpha()))
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for combo in itertools.combinations(letters, length):
            palindrome = ''.join(sorted(combo))
            palindromes.add(palindrome)
            palindromes.add(palindrome[::-1])
    return palindromes