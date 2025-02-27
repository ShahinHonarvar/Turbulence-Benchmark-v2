def palindromes_of_specific_lengths(text):
    substring = text[15:87]
    palindromes = set()
    for i in range(len(substring) - 50):
        for j in range(i + 51, i + 61):
            word = substring[i:j].lower()
            if word == word[::-1] and word.isalpha():
                palindromes.add(word)
    return palindromes