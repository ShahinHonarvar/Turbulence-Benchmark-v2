def palindromes_of_specific_lengths(s):
    substring = s[23:95].lower()
    palindromes = set()
    for length in range(17, 56):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if candidate.isalpha() and candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes