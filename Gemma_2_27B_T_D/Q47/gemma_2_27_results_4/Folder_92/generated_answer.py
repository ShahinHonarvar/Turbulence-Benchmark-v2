def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(5):
        for j in range(i + 3, min(i + 5, 5)):
            substring = text[i:j + 1].lower()
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes