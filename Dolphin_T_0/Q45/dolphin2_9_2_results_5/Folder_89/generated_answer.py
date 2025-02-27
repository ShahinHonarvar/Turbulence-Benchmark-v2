def palindromes_between_indices(s):
    letters = [c.lower() for c in s[4:10] if c.isalpha()]
    palindromes = set()
    for length in range(6, len(letters) + 1):
        for i in range(len(letters)):
            for j in range(i + length - 1, len(letters)):
                sub = letters[i:j + 1]
                if sub == sub[::-1]:
                    palindromes.add(''.join(sub))
    return palindromes