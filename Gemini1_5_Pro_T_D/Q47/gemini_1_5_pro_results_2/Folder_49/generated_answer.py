def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(10, 101):
        for j in range(i, 101):
            substring = text[i - 1:j]
            if len(substring) >= 10 and len(substring) <= 50:
                if substring.isalpha() and substring.lower() == substring.lower()[::-1]:
                    palindromes.add(substring)
    return palindromes