def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(35, 89):
        for j in range(i, 89):
            substring = text[i:j + 1]
            if 24 <= len(substring) <= 33 and substring.isalpha():
                if substring.lower() == substring.lower()[::-1]:
                    palindromes.add(substring)
    return palindromes