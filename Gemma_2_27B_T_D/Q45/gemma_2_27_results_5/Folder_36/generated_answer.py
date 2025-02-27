def palindromes_between_indices(text):
    subset = text[5:9]
    letters = ''.join(filter(str.isalpha, subset)).lower()
    palindromes = set()
    for i in range(len(letters) - 2):
        for j in range(i + 3, len(letters) + 1):
            substring = letters[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes