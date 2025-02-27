def palindromes_between_indices(text):
    letters = text[7:10]
    letters = ''.join(filter(str.isalpha, letters)).lower()
    palindromes = set()
    for i in range(len(letters) - 3):
        for j in range(i + 4, len(letters) + 1):
            substring = letters[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes