def palindromes_of_specific_lengths(text):
    palindromes = set()
    substring = text[65:100]
    for i in range(len(substring) - 25):
        for j in range(i + 26, min(i + 34, len(substring) + 1)):
            candidate = substring[i:j]
            if candidate.isalpha() and candidate.lower() == candidate.lower()[::-1]:
                palindromes.add(candidate)
    return palindromes