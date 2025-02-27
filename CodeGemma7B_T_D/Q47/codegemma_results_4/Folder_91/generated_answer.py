def palindromes_of_specific_lengths(word):
    palindromes = set()
    for i in range(10):
        for j in range(i, 11):
            substring = word[i:j + 1]
            if len(substring) >= 3 and len(substring) <= 5 and substring.isalpha():
                if substring == substring[::-1]:
                    palindromes.add(substring.lower())
    return palindromes