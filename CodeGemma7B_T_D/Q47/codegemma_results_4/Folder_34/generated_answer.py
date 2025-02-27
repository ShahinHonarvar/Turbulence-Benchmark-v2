def palindromes_of_specific_lengths(text):
    text = text.lower()
    palindromes = set()
    for i in range(200, 301):
        for j in range(i, i + 50):
            word = text[i:j]
            if word == word[::-1] and word.isalpha():
                palindromes.add(word)
    return palindromes