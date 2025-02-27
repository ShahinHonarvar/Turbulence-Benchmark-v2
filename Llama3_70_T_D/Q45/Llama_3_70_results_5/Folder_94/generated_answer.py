def palindromes_between_indices(s):
    letters = [c.lower() for c in s[3:5] if c.isalpha()]
    palindromes = set()
    for i in range(3, len(letters) + 3):
        for p in itertools.permutations(letters, i):
            palindrome = ''.join(p)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes