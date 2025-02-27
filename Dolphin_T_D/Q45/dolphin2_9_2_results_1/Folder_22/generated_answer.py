def palindromes_between_indices(s):
    substring = s[5:7]
    palindromes = set()
    for i in range(len(substring)):
        for j in range(i + 2, len(substring) + 1):
            candidate = substring[i:j]
            if len(candidate) >= 3 and candidate.lower() == candidate.lower()[::-1]:
                palindromes.add(candidate.lower())
    return palindromes