def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[5:8])).lower()
    palindromes = set()
    for i in range(len(letters) - 2):
        for j in range(i + 3, len(letters) + 1):
            substring = letters[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes