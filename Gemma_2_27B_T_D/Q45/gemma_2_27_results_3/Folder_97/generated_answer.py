def palindromes_between_indices(s):
    letters = ''.join([c for c in s[0:5] if c.isalpha()])
    lower_letters = letters.lower()
    palindromes = set()
    for i in range(len(lower_letters) - 2):
        for j in range(i + 3, len(lower_letters) + 1):
            substring = lower_letters[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes