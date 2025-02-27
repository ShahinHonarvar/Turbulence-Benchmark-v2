def palindromes_between_indices(s):
    letters = [c for c in s[3:7] if c.isalpha()]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 3, len(letters) + 1):
            substring = ''.join(letters[i:j]).lower()
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes