def palindromes_of_specific_lengths(text):
    palindromes = set()
    substring = text[124:284].lower()
    for length in range(115, 135):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if candidate == candidate[::-1] and candidate.isalpha():
                palindromes.add(candidate)
    return palindromes