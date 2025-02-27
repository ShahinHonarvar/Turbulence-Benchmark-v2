def palindromes_between_indices(s):
    s = s[2:10].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for length in range(6, len(letters) + 1):
        for i in range(len(letters)):
            for p in itertools.combinations(letters[:i] + letters[i + 1:], length - 1):
                palindrome = letters[i] + ''.join(p) + letters[i]
                palindromes.add(palindrome)
    return palindromes