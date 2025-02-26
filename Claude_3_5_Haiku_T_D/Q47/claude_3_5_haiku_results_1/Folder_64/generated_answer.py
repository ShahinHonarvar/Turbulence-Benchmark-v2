def palindromes_of_specific_lengths(s):
    palindromes = set()
    substring = s[:8].lower()
    for i in range(len(substring)):
        for j in range(i + 3, min(i + 6, len(substring) + 1)):
            candidate = substring[i:j]
            if len(candidate) in (4, 5) and candidate == candidate[::-1] and candidate.isalpha():
                palindromes.add(candidate)
    return palindromes