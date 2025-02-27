def palindromes_between_indices(string):
    letters = ''.join((char for char in string[1:5] if char.isalpha())).lower()
    palindromes = set()
    if len(letters) >= 3:
        for i in range(len(letters)):
            for j in range(i + 1, len(letters)):
                for k in range(j + 1, len(letters)):
                    substring = letters[i] + letters[j] + letters[k]
                    if substring == substring[::-1]:
                        palindromes.add(substring)
    return palindromes