def palindromes_between_indices(text):
    palindromes = set()
    for i in range(4, 10):
        for j in range(i + 2, 10):
            word = text[i:j + 1]
            word = word.lower()
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes