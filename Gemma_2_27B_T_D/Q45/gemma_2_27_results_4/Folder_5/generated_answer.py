def palindromes_between_indices(s):
    letters = s[4:9].lower().replace('.', '').replace(',', '').replace(';', '').replace(':', '').replace('!', '')
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 3, len(letters) + 1):
            substring = letters[i:j]
            if substring == substring[::-1] and len(substring) >= 4:
                palindromes.add(substring)
    return palindromes