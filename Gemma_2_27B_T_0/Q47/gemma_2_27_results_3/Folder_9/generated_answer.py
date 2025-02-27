def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(301):
        for j in range(i + 50, min(i + 61, 301)):
            substring = text[i:j].lower()
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes