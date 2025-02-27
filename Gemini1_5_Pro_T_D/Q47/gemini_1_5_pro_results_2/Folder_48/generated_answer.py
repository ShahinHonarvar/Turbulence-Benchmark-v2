def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(155, 284):
        for j in range(i + 104, min(i + 121, 284)):
            substring = text[i:j]
            if len(substring) >= 104 and len(substring) <= 120 and substring.isalpha() and (substring.lower() == substring[::-1].lower()):
                palindromes.add(substring)
    return palindromes