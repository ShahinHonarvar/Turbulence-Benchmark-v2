def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(21):
        for j in range(i + 5, min(21, i + 81)):
            substring = text[i:j]
            if len(substring) >= 5 and substring.isalpha() and (substring.lower() == substring[::-1].lower()):
                palindromes.add(substring.lower())
    return palindromes