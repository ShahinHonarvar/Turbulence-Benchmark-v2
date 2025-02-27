def palindromes_between_indices(text):
    letters = ''.join(sorted([c.lower() for c in text[6:10] if c.isalpha()]))
    palindromes = set()
    for i in range(5, len(letters) + 1):
        for j in range(i):
            word = letters[j:j + i]
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes