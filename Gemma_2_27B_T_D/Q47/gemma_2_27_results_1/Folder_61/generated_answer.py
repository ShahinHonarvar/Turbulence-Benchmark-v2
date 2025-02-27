def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(31):
        for j in range(i + 20, min(i + 31, len(text) + 1)):
            substring = text[i:j].lower()
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes