def palindromes_between_indices(s):
    letters = [c.lower() for c in s[:3] if c.isalpha()]
    palindromes = set()
    for a in letters:
        for b in letters:
            for c in letters:
                if a == b == c:
                    palindrome = a + b + c
                    if palindrome not in palindromes:
                        palindromes.add(palindrome)
    return palindromes