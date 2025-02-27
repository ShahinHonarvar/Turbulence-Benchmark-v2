def palindromes_of_specific_lengths(text):
    palindromes = set()
    substring = text[70:141]
    for i in range(len(substring) - 2):
        for j in range(i + 3, min(i + 61, len(substring))):
            word = substring[i:j]
            if word.lower() == word.lower()[::-1] and word.isalpha():
                palindromes.add(word)
    return palindromes