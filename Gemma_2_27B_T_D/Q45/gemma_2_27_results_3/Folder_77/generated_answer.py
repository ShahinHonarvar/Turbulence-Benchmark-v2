def palindromes_between_indices(text):
    subset = text[4:7]
    letters = ''.join([char for char in subset if char.isalpha()])
    palindromes = set()
    for i in range(len(letters) - 3):
        for j in range(i + 4, len(letters) + 1):
            substring = letters[i:j]
            if substring.lower() == substring[::-1].lower() and len(substring) >= 4:
                palindromes.add(substring)
    return palindromes