def palindromes_of_specific_lengths(text):
    palindromes = set()
    substring = text[35:89]
    for i in range(len(substring) - 23):
        for j in range(i + 24, min(i + 34, len(substring)) + 1):
            word = substring[i:j]
            if word.isalpha() and word.lower() == word[::-1].lower():
                palindromes.add(word)
    return palindromes