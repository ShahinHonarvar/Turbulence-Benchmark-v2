def palindromes_between_indices(text):
    letters = sorted([char for char in text[2:7] if char.isalpha()])
    palindromes = set()
    for i in range(len(letters) - 3):
        for j in range(i + 4, len(letters) + 1):
            substring = letters[i:j]
            if substring == substring[::-1]:
                palindromes.add(''.join(substring))
    return palindromes