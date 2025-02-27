def palindromes_between_indices(text):
    letters = ''.join(filter(str.isalpha, text[0:7])).lower()
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 3, len(letters) + 1):
            substring = letters[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes