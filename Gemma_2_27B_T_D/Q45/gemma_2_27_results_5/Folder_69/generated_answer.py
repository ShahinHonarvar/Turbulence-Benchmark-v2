def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[0:4])).lower()
    palindromes = set()
    for i in range(len(letters), 0, -1):
        for j in range(len(letters) - i + 1):
            substring = letters[j:j + i]
            if substring == substring[::-1] and len(substring) >= 4:
                palindromes.add(substring)
    return palindromes