def palindromes_of_specific_lengths(text):
    palindromes = set()
    substring = text[10:56]
    for i in range(len(substring)):
        for j in range(i + 3, min(i + 8, len(substring) + 1)):
            word = substring[i:j].lower()
            if word == word[::-1] and word.isalpha():
                palindromes.add(word)
    return palindromes