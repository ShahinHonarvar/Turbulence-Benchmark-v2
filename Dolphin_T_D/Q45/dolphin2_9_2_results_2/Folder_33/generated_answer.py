def palindromes_between_indices(s):
    letters = [c.lower() for c in s[6:10] if c.isalpha()]
    palindromes = set()
    for i in range(4, len(letters) + 1):
        for j in range(len(letters) - i + 1):
            if letters[j:j + i] == list(reversed(letters[j:j + i])):
                palindromes.add(''.join(letters[j:j + i]))
    return palindromes