def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(125, 284):
        for j in range(i + 108, min(284, i + 127)):
            substring = text[i:j]
            if len(substring) >= 109 and len(substring) <= 126 and substring.isalpha() and (substring.lower() == substring.lower()[::-1]):
                palindromes.add(substring)
    return palindromes