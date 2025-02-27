def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(200, 301):
        for j in range(i, min(i + 50, 301)):
            substring = text[i:j + 1]
            if len(substring) >= 10 and substring.lower() == substring[::-1].lower():
                if substring.isalpha():
                    palindromes.add(substring)
    return palindromes