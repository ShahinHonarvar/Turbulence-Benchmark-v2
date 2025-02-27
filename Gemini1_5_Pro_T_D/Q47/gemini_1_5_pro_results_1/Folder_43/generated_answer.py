def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(41, 90):
        for j in range(i + 22, min(90, i + 38)):
            substring = text[i:j + 1]
            if len(substring) >= 23 and len(substring) <= 38 and (substring.lower() == substring[::-1].lower()) and all((c.isalpha() for c in substring)):
                palindromes.add(substring)
    return palindromes