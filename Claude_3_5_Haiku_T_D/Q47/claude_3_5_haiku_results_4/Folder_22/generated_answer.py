def palindromes_of_specific_lengths(s):
    if len(s) < 201:
        return set()
    substring = s[100:201]
    palindromes = set()
    for length in range(5, 11):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            lower_candidate = candidate.lower()
            if lower_candidate == lower_candidate[::-1] and lower_candidate.isalpha():
                palindromes.add(candidate)
    return palindromes