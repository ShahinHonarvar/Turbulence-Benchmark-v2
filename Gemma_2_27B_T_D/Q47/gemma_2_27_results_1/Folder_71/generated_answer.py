def palindromes_of_specific_lengths(text):
    palindromes = set()
    substring = text[18:66]
    for i in range(len(substring) - 22):
        for j in range(i + 23, min(i + 37, len(substring) + 1)):
            word = substring[i:j]
            if word.isalpha() and word.lower() == word[::-1].lower():
                palindromes.add(word)
    return palindromes