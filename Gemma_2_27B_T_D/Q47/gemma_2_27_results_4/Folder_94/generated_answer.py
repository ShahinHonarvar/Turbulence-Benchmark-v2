def palindromes_of_specific_lengths(text):
    palindromes = set()
    substring = text[40:95]
    for i in range(len(substring) - 44):
        for j in range(i + 45, min(i + 52, len(substring)) + 1):
            candidate = substring[i:j]
            if candidate.isalpha() and candidate.lower() == candidate[::-1].lower():
                palindromes.add(candidate)
    return palindromes