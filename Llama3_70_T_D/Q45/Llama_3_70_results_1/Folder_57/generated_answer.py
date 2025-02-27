def palindromes_between_indices(s):
    letters = [c.lower() for c in s[2:6] if c.isalpha()]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 1, len(letters)):
            for k in range(len(letters)):
                if i != k and j != k:
                    palindrome = letters[i] + letters[j] + letters[k] + letters[j] + letters[i]
                    palindromes.add(palindrome)
    return palindromes