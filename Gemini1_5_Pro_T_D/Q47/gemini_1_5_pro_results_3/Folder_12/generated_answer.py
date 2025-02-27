def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(62, 88 - 17):
        for j in range(i + 17, min(i + 22, 89)):
            substring = text[i:j]
            if len(substring) >= 18 and len(substring) <= 21 and substring.isalpha() and (substring.lower() == substring[::-1].lower()):
                palindromes.add(substring)
    return palindromes