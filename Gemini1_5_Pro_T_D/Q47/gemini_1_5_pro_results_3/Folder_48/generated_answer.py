def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(155, 284):
        for j in range(i + 103, min(284, i + 121)):
            substring = text[i:j + 1]
            if len(substring) >= 104 and len(substring) <= 120 and substring.isalpha() and (substring.lower() == substring[::-1].lower()):
                palindromes.add(substring)
    return palindromes