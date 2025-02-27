def palindromes_of_specific_lengths(text):
    palindromes = set()
    substring = text[18:89]
    for i in range(len(substring) - 11):
        for j in range(i + 12, min(len(substring), i + 15)):
            candidate = substring[i:j]
            if candidate.isalpha() and candidate.lower() == candidate.lower()[::-1]:
                palindromes.add(candidate)
    return palindromes