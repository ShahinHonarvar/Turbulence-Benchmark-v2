def palindromes_between_indices(s):
    letters = [c.lower() for c in s[1:5] if c.isalpha()]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 1, len(letters)):
            palindrome = letters[i] + letters[j] + letters[i]
            palindromes.add(palindrome)
    return palindromes