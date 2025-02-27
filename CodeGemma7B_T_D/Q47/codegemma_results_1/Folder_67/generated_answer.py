def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(65, 99 + 1):
        for j in range(26, 33 + 1):
            substring = text[i:i + j + 1]
            substring = substring.lower()
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes