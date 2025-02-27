def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(101, 293):
        for j in range(i + 153, min(i + 183, 293)):
            substring = text[i:j + 1]
            if len(substring) >= 154 and len(substring) <= 182 and (substring.lower() == substring.lower()[::-1]) and all((c.isalpha() for c in substring)):
                palindromes.add(substring)
    return palindromes