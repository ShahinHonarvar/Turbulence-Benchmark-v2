def palindromes_between_indices(s):
    s = s[1:8].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 7, len(letters) + 1):
            substring = letters[i:j]
            if len(substring) >= 7 and substring == substring[::-1]:
                palindromes.add(''.join(substring))
    return palindromes