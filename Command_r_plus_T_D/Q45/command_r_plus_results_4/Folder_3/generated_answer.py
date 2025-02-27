def palindromes_between_indices(s):
    letters = [c for c in s[7:10] if c.isalpha()]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 1, len(letters)):
            palindrome = letters[i] + letters[j] + letters[i]
            palindromes.add(palindrome.lower())
            palindromes.add(palindrome.upper())
    return palindromes