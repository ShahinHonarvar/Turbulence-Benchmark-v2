def palindromes_between_indices(s):
    letters = [c for c in s[1:7].lower() if c.isalpha()]
    palindromes = set()
    for i in range(len(letters)):
        word = letters[i] + ''.join(letters[:i] + letters[i + 1:]) + letters[i]
        if len(word) >= 7:
            palindromes.add(word)
    return palindromes