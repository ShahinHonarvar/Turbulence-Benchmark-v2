def palindromes_of_specific_lengths(text):
    palindromes = set()
    substring = text[1:9]
    for i in range(len(substring) - 2):
        for j in range(i + 3, min(len(substring) + 1, i + 5)):
            word = substring[i:j].lower()
            if word == word[::-1] and word.isalpha():
                palindromes.add(word)
    return palindromes