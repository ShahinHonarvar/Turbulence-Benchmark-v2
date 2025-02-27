def palindromes_of_specific_lengths(text):
    substring = text[13:100]
    palindromes = set()
    for i in range(len(substring) - 25):
        for j in range(i + 26, min(i + 30, len(substring) + 1)):
            word = substring[i:j]
            if word.isalpha() and word.lower() == word.lower()[::-1]:
                palindromes.add(word)
    return palindromes