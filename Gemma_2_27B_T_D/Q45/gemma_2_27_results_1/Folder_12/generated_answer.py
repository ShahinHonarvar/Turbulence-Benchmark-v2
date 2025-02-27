def palindromes_between_indices(text):
    letters = ''.join(filter(str.isalpha, text[3:9])).lower()
    palindromes = set()
    for i in range(len(letters) // 2):
        for j in range(i + 1, len(letters) - i):
            substring = letters[i:j]
            if substring == substring[::-1] and len(substring) >= 4:
                palindromes.add(substring)
    return palindromes