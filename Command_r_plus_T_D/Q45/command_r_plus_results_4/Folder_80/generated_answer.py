def palindromes_between_indices(s):
    letters = [c for c in s[3:9] if c.isalpha()]
    letters = [c.lower() for c in letters]
    palindromes = set()
    for i in range(7, len(letters) + 1):
        for perm in permutations(letters, i):
            palindrome = ''.join(perm)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes