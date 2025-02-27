def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(22, 96):
        for j in range(i + 52, i + 56):
            substring = text[i:j].lower()
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes