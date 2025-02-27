def palindromes_between_indices(word):
    palindromes = set()
    for i in range(len(word)):
        for j in range(i + 4, len(word) + 1):
            substring = word[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring.lower())
    return palindromes