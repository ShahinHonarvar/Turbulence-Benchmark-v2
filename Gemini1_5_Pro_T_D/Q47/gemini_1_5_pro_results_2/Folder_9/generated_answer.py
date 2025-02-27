def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(301):
        for j in range(i, 301):
            if 50 <= j - i + 1 <= 60:
                substring = text[i:j + 1]
                if substring.isalpha() and substring.lower() == substring[::-1].lower():
                    palindromes.add(substring)
    return palindromes