def palindromes_of_specific_lengths(text):
    palindromes = set()
    substring = text[41:90]
    for i in range(len(substring) - 22):
        for j in range(i + 23, min(i + 39, len(substring) + 1)):
            word = substring[i:j]
            if word.lower() == word.lower()[::-1] and word.isalpha():
                palindromes.add(word)
    return palindromes