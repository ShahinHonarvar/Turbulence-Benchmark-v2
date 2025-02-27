def palindromes_between_indices(text):
    letters = text[7:9].lower()
    palindromes = set()
    for i in range(len(letters), 0, -1):
        for j in range(0, len(letters) - i + 1):
            substring = letters[j:j + i]
            if substring == substring[::-1] and len(substring) >= 3:
                palindromes.add(substring)
    return palindromes