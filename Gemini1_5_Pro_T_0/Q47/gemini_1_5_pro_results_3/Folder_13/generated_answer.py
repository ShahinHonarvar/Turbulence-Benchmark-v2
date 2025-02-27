def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(13, 95):
        for j in range(57, 61):
            if i + j <= 96:
                substring = text[i:i + j]
                if len(substring) >= 57 and len(substring) <= 60 and substring.isalpha() and (substring.lower() == substring.lower()[::-1]):
                    palindromes.add(substring)
    return palindromes