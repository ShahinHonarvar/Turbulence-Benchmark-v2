def palindromes_between_indices(text):
    letters = text[1:8].lower()
    palindromes = set()
    for i in range(3, len(letters) + 1):
        for j in range(len(letters) - i + 1):
            substring = letters[j:j + i]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes