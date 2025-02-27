def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(10, 56):
        for j in range(i + 3, min(i + 8, 56)):
            substring = text[i:j].lower()
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes