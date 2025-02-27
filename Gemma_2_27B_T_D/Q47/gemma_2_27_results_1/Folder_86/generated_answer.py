def palindromes_of_specific_lengths(text):
    palindromes = set()
    substring = text[30:96]
    for i in range(len(substring) - 33):
        for j in range(i + 34, min(i + 56, len(substring)) + 1):
            word = substring[i:j]
            if word.isalpha() and word.lower() == word[::-1].lower():
                palindromes.add(word)
    return palindromes