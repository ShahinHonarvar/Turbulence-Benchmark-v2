def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(40, 95):
        for j in range(i, 95):
            if 45 <= j - i + 1 <= 51:
                substring = text[i:j + 1]
                if substring.isalpha() and substring.lower() == substring[::-1].lower():
                    palindromes.add(substring)
    return palindromes