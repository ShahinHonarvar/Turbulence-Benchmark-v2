def palindromes_of_specific_lengths(text):
    palindromes = set()
    substring = text[1:300]
    for i in range(len(substring) - 2):
        for j in range(i + 3, min(i + 11, len(substring) + 1)):
            word = substring[i:j].lower()
            if word == word[::-1] and word.isalpha():
                palindromes.add(word)
    return palindromes