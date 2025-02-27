def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(119, 256 - 103):
        for j in range(104, min(124, 257 - i)):
            substring = text[i:i + j].lower()
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes