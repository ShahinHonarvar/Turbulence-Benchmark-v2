def palindromes_of_specific_lengths(text):
    palindromes = set()
    substring = text[0:5]
    for i in range(len(substring) - 3):
        for j in range(i + 3, min(len(substring), i + 5)):
            word = substring[i:j]
            if word.isalpha() and word.lower() == word.lower()[::-1]:
                palindromes.add(word)
    return palindromes