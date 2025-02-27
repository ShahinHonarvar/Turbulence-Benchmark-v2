def palindromes_of_specific_lengths(text):
    palindromes = set()
    substring = text[29:97]
    for i in range(len(substring) - 11):
        for j in range(i + 12, min(i + 19, len(substring)) + 1):
            word = substring[i:j]
            if word.isalpha() and word.lower() == word.lower()[::-1]:
                palindromes.add(word)
    return palindromes