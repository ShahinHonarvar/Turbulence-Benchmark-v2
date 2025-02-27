def palindromes_between_indices(s):
    letters = [c for c in s[1:7] if c.isalpha()]
    palindromes = set()
    for p in range(4, len(letters) + 1):
        for i in range(len(letters) - p + 1):
            if letters[i:i + p] == list(reversed(letters[i:i + p])):
                palindromes.add(''.join(letters[i:i + p]).lower())
    return palindromes