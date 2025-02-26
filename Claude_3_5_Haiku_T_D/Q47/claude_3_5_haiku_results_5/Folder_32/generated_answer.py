def palindromes_of_specific_lengths(s):
    palindromes = set()
    substring = s[16:78]
    for length in range(43, 48):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if candidate.lower() == candidate.lower()[::-1] and candidate.isalpha():
                palindromes.add(candidate)
    return palindromes