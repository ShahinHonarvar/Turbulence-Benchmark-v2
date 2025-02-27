def palindromes_between_indices(text):
    letters = ''.join((char for char in text[1:8] if char.isalpha())).lower()
    palindromes = set()
    for i in range(len(letters) - 2):
        for j in range(i + 2, len(letters) + 1):
            substring = letters[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes