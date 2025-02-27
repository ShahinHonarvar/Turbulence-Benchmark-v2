def palindromes_of_specific_lengths(text):
    palindromes = set()
    substring = text[100:201]
    for i in range(len(substring) - 4):
        for j in range(i + 5, min(i + 11, len(substring) + 1)):
            word = substring[i:j].lower()
            if word == word[::-1] and word.isalpha():
                palindromes.add(word)
    return palindromes