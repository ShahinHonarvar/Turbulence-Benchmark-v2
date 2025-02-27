def palindromes_of_specific_lengths(text):
    palindromes = set()
    for start in range(300):
        for end in range(50, 61):
            substring = text[start:end]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes