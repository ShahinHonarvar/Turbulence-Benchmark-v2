def palindromes_between_indices(s):
    s = s[2:8].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for i in range(len(letters) - length + 1):
            for j in range(i + length // 2 + length % 2, len(letters)):
                substring = letters[i:i + length // 2] + letters[i + length // 2:j + 1][::-1]
                if len(substring) >= 3:
                    palindromes.add(''.join(substring))
    return palindromes