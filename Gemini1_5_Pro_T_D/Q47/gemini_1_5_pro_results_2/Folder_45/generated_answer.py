def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(70, 141):
        for j in range(i + 3, min(len(text) + 1, i + 61)):
            substring = text[i:j]
            if 3 <= len(substring) <= 60 and substring.isalpha() and (substring.lower() == substring[::-1].lower()):
                palindromes.add(substring)
    return palindromes