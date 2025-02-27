def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(13, 99 - 25):
        for length in range(26, 30):
            substring = text[i:i + length].lower()
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(text[i:i + length])
    return palindromes