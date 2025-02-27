def palindromes_between_indices(s):
    letters = [c for c in s[2:7] if c.isalpha()]
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for i in range(len(letters) - length + 1):
            substring = ''.join(letters[i:i + length]).lower()
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes