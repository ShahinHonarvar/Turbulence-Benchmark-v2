def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(63, 67):
        for j in range(i + 3, min(i + 5, 71)):
            substring = text[i:j + 1]
            if substring.isalpha() and substring.lower() == substring[::-1].lower():
                palindromes.add(substring.lower())
    return palindromes