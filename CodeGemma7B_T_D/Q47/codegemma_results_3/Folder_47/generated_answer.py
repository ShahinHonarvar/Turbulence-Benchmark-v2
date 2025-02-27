def palindromes_of_specific_lengths(text):
    palindromes = set()
    text = text[39:95].lower()
    for i in range(len(text) - 13):
        for end in range(i + 14, len(text) + 1):
            substring = text[i:end]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes