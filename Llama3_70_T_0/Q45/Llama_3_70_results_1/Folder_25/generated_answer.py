def palindromes_between_indices(s):
    s = s[1:5].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 1, len(letters)):
            for k in range(j + 1, len(letters)):
                for c in letters:
                    palindrome = letters[i] + letters[j] + letters[k] + c + letters[k] + letters[j] + letters[i]
                    palindromes.add(palindrome)
    return palindromes