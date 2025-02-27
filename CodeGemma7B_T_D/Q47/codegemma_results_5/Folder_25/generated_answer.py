def palindromes_of_specific_lengths(str1):
    palindromes = set()
    for i in range(26, 85):
        for j in range(i - 29, i + 1):
            word = str1[j:i + 1]
            if word == word[::-1] and word.isalpha():
                palindromes.add(word.lower())
    return palindromes