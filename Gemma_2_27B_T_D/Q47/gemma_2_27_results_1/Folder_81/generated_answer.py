def palindromes_of_specific_lengths(text):
    palindromes = set()
    substring = text[12:122]
    for i in range(len(substring)):
        for j in range(i, len(substring)):
            word = substring[i:j + 1].lower()
            if word == word[::-1] and 12 <= len(word) <= 220 and word.isalpha():
                palindromes.add(word)
    return palindromes