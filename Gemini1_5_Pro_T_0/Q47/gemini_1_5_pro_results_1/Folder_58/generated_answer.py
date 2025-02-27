def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(125, 283 + 1):
        for j in range(i, 283 + 1):
            if 109 <= j - i + 1 <= 126:
                substring = text[i:j + 1]
                if substring.isalpha() and substring.lower() == substring[::-1].lower():
                    palindromes.add(substring)
    return palindromes