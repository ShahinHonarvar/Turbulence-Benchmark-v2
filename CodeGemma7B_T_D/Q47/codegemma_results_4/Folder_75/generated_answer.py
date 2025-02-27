def palindromes_of_specific_lengths(text):
    text = text.lower()
    substring = text[31:75]
    palindromes = set()
    for length in range(23, 40):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if candidate.isalpha():
                palindromes.add(candidate)
    return palindromes