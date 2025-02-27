def palindromes_of_specific_lengths(text):
    text = text[17:73].lower()
    palindromes = set()
    for i in range(len(text) - 50 + 1):
        for j in range(i + 50, min(i + 52, len(text) + 1)):
            substring = text[i:j]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes