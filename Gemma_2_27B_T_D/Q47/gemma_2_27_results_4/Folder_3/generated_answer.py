def palindromes_of_specific_lengths(text):
    substring = text[27:96]
    palindromes = set()
    for i in range(len(substring) - 49 + 1):
        for j in range(i + 49, i + 52):
            word = substring[i:j]
            if word.lower() == word.lower()[::-1] and word.isalpha():
                palindromes.add(word)
    return palindromes