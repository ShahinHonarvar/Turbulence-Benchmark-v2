def palindromes_of_specific_lengths(s):
    substring = s[11:84].lower()
    palindromes = set()
    for length in range(13, 67):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if candidate.isalpha() and candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes