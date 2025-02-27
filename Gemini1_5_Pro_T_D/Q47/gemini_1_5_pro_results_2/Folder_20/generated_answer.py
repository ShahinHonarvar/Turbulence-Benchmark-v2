def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(20, 74 - 35):
        for length in range(36, 43):
            substring = text[i:i + length].lower()
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(text[i:i + length])
    return palindromes