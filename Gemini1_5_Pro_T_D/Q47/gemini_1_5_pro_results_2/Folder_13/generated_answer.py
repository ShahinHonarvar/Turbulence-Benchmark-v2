def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(13, 95 - 56):
        for j in range(i + 57, min(i + 61, 96)):
            substring = text[i:j]
            if len(substring) >= 57 and len(substring) <= 60 and substring.isalpha() and (substring.lower() == substring[::-1].lower()):
                palindromes.add(substring)
    return palindromes