def palindromes_of_specific_lengths(s):
    palindromes = set()
    substring = s[62:89]
    for length in range(18, 22):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if candidate.lower() == candidate.lower()[::-1] and candidate.isalpha():
                palindromes.add(candidate)
    return palindromes