def palindromes_of_specific_lengths(text):
    palindromes = set()
    text = text.lower().replace(' ', '')
    for i in range(30, 96):
        for j in range(i + 33, 96):
            word = text[i:j]
            if word == word[::-1] and len(word) in range(34, 56):
                palindromes.add(word)
    return palindromes