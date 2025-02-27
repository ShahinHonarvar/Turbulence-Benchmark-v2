def palindromes_between_indices(s):
    palindromes = set()
    letters = [c for c in s[3:8] if c.isalpha()]
    for i in range(5, len(letters) + 1):
        for x in combinations(letters, i):
            word = ''.join(x)
            for y in permutations(word):
                palindrome = ''.join(y)
                if palindrome == palindrome[::-1]:
                    palindromes.add(palindrome.lower())
    return palindromes