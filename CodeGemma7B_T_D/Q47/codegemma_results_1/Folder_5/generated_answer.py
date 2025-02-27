def palindromes_of_specific_lengths(text):
    text = text.lower()
    palindromes = set()
    for i in range(63, 71):
        for j in range(i - 5, i):
            word = text[j:i + 1]
            if word == word[::-1] and word.isalpha():
                palindromes.add(word)
    return palindromes