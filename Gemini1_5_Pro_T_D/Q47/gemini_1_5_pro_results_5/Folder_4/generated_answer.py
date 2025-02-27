def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(12, 93):
        for j in range(i + 16, min(i + 66, 93) + 1):
            substring = text[i:j]
            if len(substring) >= 17 and len(substring) <= 66 and (substring.lower() == substring.lower()[::-1]) and all((char.isalpha() for char in substring)):
                palindromes.add(substring)
    return palindromes