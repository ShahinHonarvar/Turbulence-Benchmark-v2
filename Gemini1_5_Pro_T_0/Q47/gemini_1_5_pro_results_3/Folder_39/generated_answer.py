def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(31, 92):
        for j in range(i + 49, i + 53):
            if j <= 91:
                substring = text[i:j + 1]
                if len(substring) >= 50 and len(substring) <= 53 and substring.isalpha() and (substring.lower() == substring[::-1].lower()):
                    palindromes.add(substring)
    return palindromes