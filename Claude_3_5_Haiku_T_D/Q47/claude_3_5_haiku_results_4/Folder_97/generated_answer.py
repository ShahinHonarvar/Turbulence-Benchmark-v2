def palindromes_of_specific_lengths(text):
    if len(text) < 95:
        return set()
    substring = text[28:95].lower()
    palindromes = set()
    for length in range(38, 50):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if candidate == candidate[::-1] and candidate.isalpha():
                palindromes.add(candidate)
    return palindromes