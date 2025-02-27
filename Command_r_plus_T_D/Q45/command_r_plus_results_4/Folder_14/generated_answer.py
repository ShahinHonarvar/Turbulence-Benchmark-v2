def palindromes_between_indices(s):
    letters = ''.join((c for c in s[4:6] if c.isalpha())).lower()
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 3, len(letters) + 1):
            palindromes.add(letters[i:j] + letters[i:j][::-1])
    return palindromes