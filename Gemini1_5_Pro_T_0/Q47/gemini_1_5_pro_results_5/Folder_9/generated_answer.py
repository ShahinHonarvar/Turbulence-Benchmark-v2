def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(301):
        for j in range(i + 50, min(i + 61, 301)):
            substring = text[i:j]
            if len(substring) >= 50 and len(substring) <= 60 and (substring.lower() == substring.lower()[::-1]) and all((letter.isalpha() for letter in substring)):
                palindromes.add(substring)
    return palindromes