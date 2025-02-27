def palindromes_of_specific_lengths(text):
    palindromes = set()
    substring = text[75:96]
    for i in range(len(substring) - 6):
        for j in range(i + 7, len(substring) + 1):
            word = substring[i:j]
            if word.isalpha() and word.lower() == word.lower()[::-1] and (7 <= len(word) <= 9):
                palindromes.add(word)
    return palindromes