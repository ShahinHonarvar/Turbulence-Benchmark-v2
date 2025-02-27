def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(3, 301):
        substring = text[i:i + 300]
        for j in range(len(substring) - 29):
            word = substring[j:j + 30]
            if word.isalpha() and word.lower() == word[::-1].lower() and (30 <= len(word) <= 300):
                palindromes.add(word)
    return palindromes