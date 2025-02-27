def palindromes_between_indices(s):
    letters = s[1:3]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 1, len(letters)):
            for k in range(j + 1, len(letters)):
                substring = letters[i:k + 1].lower()
                if substring == substring[::-1] and len(substring) >= 3:
                    palindromes.add(substring)
    return palindromes